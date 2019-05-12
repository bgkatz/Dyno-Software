%%%% Setup Parameters %%%%
cmd_max_envelope = [18, 18, 18, 18, 18, 18, 15, 12, 9, 6, 3];   %%% maximum command
cmd_min_envelope = -[18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18];
speed_envelope = [1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200];     
speed_intervals = 25;       %%% Speed setpoints
cmd_intervals = 10;         %%% Torque setpoints
sample_length = .75;          %%% Seconds per test point
break_length = .1;           %%% Seconds between test points
settling_time = 1.0;            %%% Setpoint settling time
dt = .02;                   %%% Time step 
slew_rate = 30;             %%% Max Rad/s^2
voltage = 22;

%%%%%%%%

delta_speed = slew_rate*dt;
time_vec = [0];
speed_vec = [0];
cmd_vec = [0];
flag_vec = [0];

speeds = linspace(min(speed_envelope), max(speed_envelope), speed_intervals);

for i = 1:speed_intervals
    %%% Ramp up speed %%%
    while(speed_vec(end) < speeds(i))
        time_vec = [time_vec; time_vec(end)+dt];
        speed_vec = [speed_vec; speed_vec(end)+delta_speed];
        cmd_vec = [cmd_vec; 0];
        flag_vec = [flag_vec; 0];
    end
    %%% Speed Settling Period %%%
    for k = 1:floor(settling_time/dt)
        time_vec = [time_vec; time_vec(end)+dt];
        speed_vec = [speed_vec; speeds(i)];
        cmd_vec = [cmd_vec; 0];
        flag_vec = [flag_vec; 0];
    end
    commands = [linspace(interp1(speed_envelope, cmd_min_envelope, speeds(i)), 0, cmd_intervals),...
        linspace(0, interp1(speed_envelope, cmd_max_envelope, speeds(i)), cmd_intervals)];
    for j = 1:2*cmd_intervals;
        %%% Torque Settling Period
        for k = 1:floor(.2*sample_length/dt)
            %command = (j/cmd_intervals)*interp1(speed_envelope, cmd_max_envelope, speeds(i));
            command = commands(j);
            time_vec = [time_vec; time_vec(end)+dt];
            speed_vec = [speed_vec; speeds(i)];
            cmd_vec = [cmd_vec; command];
            flag_vec = [flag_vec; 0];
        end
        %%% Sample Period %%%
        for k = 1:floor(sample_length/dt)
            %command = (j/cmd_intervals)*interp1(speed_envelope, cmd_max_envelope, speeds(i));
            command = commands(j);
            time_vec = [time_vec; time_vec(end)+dt];
            speed_vec = [speed_vec; speeds(i)];
            cmd_vec = [cmd_vec; command];
            flag_vec = [flag_vec; (command>0)+1];
        end
        %%% Break Period %%%
        for k = 1:floor(break_length/dt)
            time_vec = [time_vec; time_vec(end)+dt];
            speed_vec = [speed_vec; speeds(i)];
            cmd_vec = [cmd_vec; cmd_vec(end)];
            flag_vec = [flag_vec; 0];
        end
    end
end

voltage_vec = voltage*ones(length(time_vec), 1);
series = [time_vec, cmd_vec, -1*speed_vec, voltage_vec, flag_vec];
figure;plot(series);
csvwrite('emap.csv', series);