module lif_neuron #(
    parameter WIDTH = 8,           // Bit width of the potential
    parameter LEAK = 8'd200,       // λ scaled: e.g., 0.8 * 256 = 204
    parameter SCALE = 8'd256,      // Fixed-point scale factor
    parameter THRESHOLD = 8'd128,  // Threshold to spike
    parameter RESET_VAL = 8'd0     // Reset value for potential
)(
    input logic clk,
    input logic rst,
    input logic I,                 // Binary input
    output logic S                // Output spike
);

    logic [WIDTH-1:0] P;          // Membrane potential
    logic [WIDTH-1:0] P_next;

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            P <= RESET_VAL;
            S <= 0;
        end else begin
            if (S)
                P <= RESET_VAL;
            else
                P <= P_next;

            S <= (P_next >= THRESHOLD) ? 1 : 0;
        end
    end

    // Compute P_next = λ*P + I
    always_comb begin
        P_next = ((P * LEAK) >> 8) + I;
    end

endmodule
