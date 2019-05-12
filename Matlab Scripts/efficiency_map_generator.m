%%%% Setup Parameters %%%%
cmd_max_envelope = [5000, 5000, 1000];   %%% maximum command
cmd_min_envelope = [-5000, -5000, -5000];
speed_envelope = [1, 21.0, 28];    
%cmd_max_envelope = [0, 0];
%cmd_min_envelope = [-4000, -4000];
%speed_envelope = [3.9, 4];
voltage_envelope = [0, 40];
speed_intervals = 15;       %%% Speed setpoints
cmd_intervals = 30;         %%% Torque setpoints
sample_length = 2.0;          %%% Seconds per test point
break_length = .5;     d      %%% Seconds between test points
settling_time = 1.0;            %%% speed Setpoint settling time
dt = .02;                   %%% Time step 
slew_rate = 30;             %%% Max Rad/s^2
voltage = 24;

%%%%%%%%

delta_speed = slew_rate*dt;
time_vec = [0];
speed_vec = [0];
cmd_vec = [0];
flag_vec = [0];
p1_vec = [0];
p2_vec = [0];


speeds = linspace(min(speed_envelope), max(speed_envelope), speed_intervals);

for i = 1:speed_intervals
    %%% Ramp up speed %%%
    while(speed_vec(end) < speeds(i))
        time_vec = [time_vec; time_vec(end)+dt];
        speed_vec = [speed_vec; speed_vec(end)+delta_speed];
        cmd_vec = [cmd_vec; 0];
        flag_vec = [flag_vec; 0];
        p1_vec = [p1_vec; 0];
        p2_vec = [p2_vec; 0];
    end
    %%% Speed Settling Period %%%
    for k = 1:floor(settling_time/dt)
        time_vec = [time_vec; time_vec(end)+dt];
        speed_vec = [speed_vec; speeds(i)];
        cmd_vec = [cmd_vec; 0];
        flag_vec = [flag_vec; 0];
        p1_vec = [p1_vec; 0];
        p2_vec = [p2_vec; 0];
    end
    for j = 1:cmd_intervals;
        %%% Torque Settling Period
        c_min = interp1(speed_envelope, cmd_min_envelope, speeds(i));
        c_max = interp1(speed_envelope, cmd_max_envelope, speeds(i));
        cmd_ints = linspace(c_min, c_max, cmd_intervals);
        for k = 1:floor(.2*sample_length/dt)
            %command = (j/cmd_intervals)*interp1(speed_envelope, cmd_max_envelope, speeds(i));
            command = cmd_ints(j);
            time_vec = [time_vec; time_vec(end)+dt];
            speed_vec = [speed_vec; speeds(i)];
            cmd_vec = [cmd_vec; command];
            flag_vec = [flag_vec; 0];
            p1_vec = [p1_vec; 0];
            p2_vec = [p2_vec; 0];
        end
        %%% Sample Period %%%
        for k = 1:floor(sample_length/dt)
            %command = (j/cmd_intervals)*interp1(speed_envelope, cmd_max_envelope, speeds(i));
            command = cmd_ints(j);
            time_vec = [time_vec; time_vec(end)+dt];
            speed_vec = [speed_vec; speeds(i)];
            cmd_vec = [cmd_vec; command];
            flag_vec = [flag_vec; 1];
            p1_vec = [p1_vec; 0];
            p2_vec = [p2_vec; 0];
        end
        %%% Break Period %%%
        for k = 1:floor(break_length/dt)
            time_vec = [time_vec; time_vec(end)+dt];
            speed_vec = [speed_vec; speeds(i)];
            cmd_vec = [cmd_vec; cmd_vec(end)];
            flag_vec = [flag_vec; 0];
            p1_vec = [p1_vec; 0];
            p2_vec = [p2_vec; 0];
        end
    end
end

voltage_vec = voltage*ones(length(time_vec), 1);
series = [time_vec, cmd_vec, -1*speed_vec, voltage_vec, flag_vec, p1_vec, p2_vec];
figure;plot(series);
csvwrite('emap.csv', series);