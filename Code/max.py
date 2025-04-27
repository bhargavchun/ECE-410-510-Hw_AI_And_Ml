module MaxFinder #(parameter WIDTH = 16) (
input logic [WIDTH-1:0] q0, q1, q2, q3,
output logic [WIDTH-1:0] max_q,
output logic [1:0] max_action
);

logic [WIDTH-1:0] max0, max1;
logic [1:0] action0, action1;

// First level comparisons
always_comb begin
if (q0 >= q1) begin
max0 = q0;
action0 = 2'd0;
end else begin
max0 = q1;
action0 = 2'd1;
end

if (q2 >= q3) begin
max1 = q2;
action1 = 2'd2;
end else begin
max1 = q3;
action1 = 2'd3;
end
end

// Second level comparison
always_comb begin
if (max0 >= max1) begin
max_q = max0;
max_action = action0;
end else begin
max_q = max1;
