module tb_lif_neuron;

    logic clk, rst, I;
    logic S;

    // Instantiate neuron
    lif_neuron #(
        .WIDTH(8),
        .LEAK(8'd200),        // ~λ = 0.78
        .SCALE(8'd256),
        .THRESHOLD(8'd128),
        .RESET_VAL(8'd0)
    ) neuron (
        .clk(clk),
        .rst(rst),
        .I(I),
        .S(S)
    );

    // Clock generation
    initial clk = 0;
    always #5 clk = ~clk;

    // Stimulus
    initial begin
        $display("Time\tI\tS");
        $monitor("%4t\t%b\t%b", $time, I, S);

        // Reset
        rst = 1; I = 0; #10;
        rst = 0;

        // --- 1. Constant input below threshold ---
        $display("\n--- Constant input below threshold ---");
        repeat (10) begin I = 1; #10; end

        // --- 2. Input accumulates until reaching threshold ---
        $display("\n--- Accumulating input ---");
        rst = 1; #10; rst = 0;
        repeat (20) begin I = 1; #10; end

        // --- 3. Leakage with no input ---
        $display("\n--- Leakage with no input ---");
        rst = 1; #10; rst = 0;
        I = 1; #30; I = 0;
        repeat (10) #10;

        // --- 4. Strong input causing immediate spike ---
        $display("\n--- Strong input causing spike ---");
        rst = 1; #10; rst = 0;
        I = 1;
        force neuron.P = 8'd150;  // Manually set potential
        #10;
        release neuron.P;

        #50 $finish;
    end

endmodule
