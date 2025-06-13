module scan_chain_tb;

  parameter CHAIN_LEN = 8;
  reg clk, scan_in, test_mode, reset;
  wire scan_out;

  reg [CHAIN_LEN-1:0] scan_chain;
  integer i, fout;

  // Simulate a stuck-at fault
  parameter integer FAULT_POS = 3;
  parameter bit FAULT_TYPE = 1'b0;  // stuck-at-0

  initial begin
    clk = 0;
    forever #5 clk = ~clk;
  end

  initial begin
    reset = 1;
    #10 reset = 0;
  end

  always @(posedge clk or posedge reset) begin
    if (reset) begin
      scan_chain <= '0;
    end else if (test_mode) begin
      scan_chain <= {scan_in, scan_chain[CHAIN_LEN-1:1]};
      
      // Inject stuck-at fault
      scan_chain[FAULT_POS] <= FAULT_TYPE;
    end
  end

  assign scan_out = scan_chain[0];

  initial begin
    test_mode = 1;

    // Open CSV output file
    fout = $fopen("scan_results.csv", "w");
    $fwrite(fout, "scan_len,pattern_bit,fault_pos,fault_type,scan_out\n");

    for (i = 0; i < 16; i++) begin
      scan_in = i[0];
      #10;
      $fwrite(fout, "%0d,%0d,%0d,%0d,%0d\n", CHAIN_LEN, scan_in, FAULT_POS, FAULT_TYPE, scan_out);
    end

    $fclose(fout);
    $finish;
  end

endmodule
