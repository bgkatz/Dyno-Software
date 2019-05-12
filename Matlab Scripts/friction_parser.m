%data = load('vs_gearbox_loss_3.csv');
time = data(:,1); 
torque = -data(:,2);
speed = -data(:,3);
voltage = data(:,4);
current = data(:,5);
flag = data(:,9);
motor_current = .001*(data(:,10));
kt = 53*.014;   % N-m/A * gear ratio

torque_points = [];
speed_points = [];
voltage_points = [];
current_points = [];
motor_current_points = [];


start_ind = find(diff(flag)>0);
stop_ind = find(diff(flag)<0);

for i = 1:length(start_ind);
    t_next = mean(torque(start_ind(i):stop_ind(i)));
        torque_points = [torque_points, mean(torque(start_ind(i):stop_ind(i)))];
        speed_points = [speed_points, mean(speed(start_ind(i):stop_ind(i)))];
        voltage_points = [voltage_points, mean(voltage(start_ind(i):stop_ind(i)))];
        current_points = [current_points, mean(current(start_ind(i):stop_ind(i)))];
        motor_current_points = [motor_current_points, mean(motor_current(start_ind(i):stop_ind(i)))];
    
end

% Tests run at constant speed, with positive and negative torque, rather
% than all positive torques, and positive and negative speed. These are
% equivalent though.
t_expected = kt*motor_current_points;
t_pos_work = torque_points(8:end);
t_neg_work = torque_points(2:8);
t_exp1 = t_expected(8:end);
t_exp2 = t_expected(2:8);

figure; hold all;
plot(t_exp1, t_exp1);
plot(t_exp1, t_pos_work);
plot(-t_exp2, -t_neg_work);
xlim([0 max(t_exp1)]);
ylim([0, max(-t_neg_work)]);
xlabel('Expected Torque (kt * GearRatio)(N-m)');
ylabel('Measured Torque (N-m)');
legend('Expected Torque', 'Positive Work', 'Negative Work');
NicePlot;
%saveas(gcf, 'friction.bmp');

