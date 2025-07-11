module decoder (
  input logic [31:0] instruction,
  output logic [6:0] opcode,
  output logic [2:0] funct3,
  output logic [6:0] funct7
);

  assign opcode = instruction[6:0];
  assign funct3 = instruction[14:12];
  assign funct7 = instruction[31:25];

  initial begin
    $dumpfile("wave.vcd");
    $dumpvars(0, decoder);
  end

endmodule

