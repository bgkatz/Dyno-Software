docname = 'vicarious_maxon';

time = data(:,1); 
torque = -data(:,2);
speed = -data(:,3);
voltage = data(:,4);
current = data(:,5);
flag = data(:,8);

torque_points = [];
speed_points = [];
voltage_points = [];
current_points = [];


start_ind = find(diff(flag)>0);
stop_ind = find(diff(flag)<0);

for i = 1:length(start_ind);
    t_next = mean(torque(start_ind(i):stop_ind(i)));
    if(t_next>0)
        torque_points = [torque_points, mean(torque(start_ind(i):stop_ind(i)))];
        speed_points = [speed_points, mean(speed(start_ind(i):stop_ind(i)))];
        voltage_points = [voltage_points, mean(voltage(start_ind(i):stop_ind(i)))];
        current_points = [current_points, mean(current(start_ind(i):stop_ind(i)))];
    end
end

pm = torque_points.*speed_points;
pe = voltage_points.*current_points;
efficiency = pm./pe;
loss = abs(pm-pe);


figure;
scatter3(speed_points, torque_points, efficiency, 50, efficiency, 'filled');
colormap(jet); colorbar; xlabel('Speed (rad/s)'); ylabel('Torque (N-m)'); zlabel('Efficiency');


figure;
scatter3(speed_points, current_points, torque_points, 50, 'filled');
colormap(jet); colorbar; xlabel('Speed (rad/s)'); ylabel('Current (A)'); zlabel('N-m');

%  figure;
%  scatter3(speed_points, torque_points, loss, 50, loss, 'filled');
%  colormap(jet); colorbar; xlabel('Speed (rad/s)'); ylabel('Torque (N-m)'); zlabel('Loss (W)');

n = 30;
n2 = 30;

speed_points = 1/n*speed_points;
s_range = linspace(min(speed_points), max(speed_points), n2);
t_range = linspace(min(torque_points), max(torque_points),n2);

t_pos = linspace(0, max(torque_points), n2);
eff_pos = efficiency(1:floor(length(efficiency)/2));
[s_grid_small, t_grid_small] = meshgrid(s_range, t_pos);
%eff_grid = griddata(speed_points(1:floor(length(efficiency)/2)), torque_points(1:floor(length(efficiency)/2)), eff_pos, s_grid_small, t_grid_small);

% Turn the scattered data into evenly spaced grids %
[s_grid, t_grid] = meshgrid(s_range, t_range);
eff_grid = griddata(speed_points, torque_points, efficiency, s_grid, t_grid);
loss_grid = griddata(speed_points, torque_points, loss, s_grid, t_grid);
pe_grid = griddata(speed_points, torque_points, pe, s_grid, t_grid);

% figure;
% surf(50*s_grid, t_grid, eff_grid);
% colormap(jet);
% xlabel('Speed (rad/s)'); ylabel('Torque (N-m)'); zlabel('Efficiency');

h1 = figure;
[c, h] = contourf(n*s_grid_small, t_grid_small, eff_grid, 15);  %for 2 quadrant data
%[c, h] = contourf(n*s_grid, t_grid, eff_grid, 15);             %for single quadrant data
clabel(c, h, 'FontSize', 8);
colormap(jet);
colorbar; 
xlabel('Speed (rad/s)'); ylabel('Torque (N-m)'); zlabel('Efficiency');
title('Efficiency Map');
set(h1, 'Position', [100, 100, 800, 600]);

print('1', '-dsvg');
% figure;
% surf(50*s_grid, t_grid, loss_grid);
% colormap(jet);
% xlabel('Speed (rad/s)'); ylabel('Torque (N-m)'); zlabel('Loss (W)');

h2 = figure;
[c, h] = contourf(n*s_grid, t_grid, loss_grid, 15);
clabel(c, h, 'FontSize', 8);
colormap(jet);
colorbar; 
xlabel('Speed (rad/s)'); ylabel('Torque (N-m)'); zlabel('Loss (W)');
title('Loss Map')
set(h2, 'Position', [100, 100, 800, 600]);

print('2', '-dsvg');

h3 = figure;
[c, h] = contourf(n*s_grid, t_grid, pe_grid, 15);
clabel(c, h, 'FontSize', 8);
hold on;
[c, h] = contour(n*s_grid, t_grid, pe_grid, [0, 0], 'LineWidth', 2, 'LineColor', 'R');
clabel(c, h, 'FontSize', 8, 'Color', 'red');
hold off
colormap(jet);
colorbar; 
xlabel('Speed (rad/s)'); ylabel('Torque (N-m)'); zlabel('Electrical Power (W)');
title('Input Power Map');
set(h3, 'Position', [100, 100, 800, 600]);

%set(h1, 'Position', [100, 100, 800, 1800]);
print('3', '-dsvg');


motorname = ('ex-8');
kt = '.11 N-m/(Peak phase Amp)';
r = '0.039 Ohms';
l = '0.38 milli Henries';
vtest = '50 Volts';
itest = '50 Battery Amps';


import mlreportgen.dom.*;
report = Document('motter', 'pdf');
open(report);
s = report.CurrentPageLayout;
s.PageMargins.Left = '.5in';
s.PageMargins.Right = '.5in';

heading = Heading(1, motorname);
heading.HAlign = 'center';
heading.Underline = 'single';
append(report, heading);

specs1 = Text(['Test Voltage:  ', vtest]);
specs2 = Text(['Test Current:  ', itest]);
specs3 = Text(['Torque Constant:  ', kt]);
specs4 = Text(['Line-to-line Resistance:  ', r]);
specs5 = Text(['Line-to-line Inductance: ', l]);
append(report, specs1);
append(report, specs2);
append(report, specs3);
append(report, specs4);
append(report, specs5);

im1 = Image('1.svg');
im1.Width = '7.5in';
im2 = Image('2.svg');
im2.Width = '7.5in';
im3 = Image('3.svg');
im3.Width = '7.5in';
append(report, im1);
append(report, im2);
append(report, im3);
close(report);

csvwrite(docname, data);
%append_pdfs(docname, '1.pdf', '2.pdf', '3.pdf')