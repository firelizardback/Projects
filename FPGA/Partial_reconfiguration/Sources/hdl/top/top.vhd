library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity top is
    Port ( clk : in STD_LOGIC);
end top;

architecture Behavioral of top is

COMPONENT vio_test
  PORT (
    clk         : IN STD_LOGIC;
    probe_in0   : IN STD_LOGIC_VECTOR(127 DOWNTO 0);
    probe_in1   : IN STD_LOGIC_VECTOR(0 DOWNTO 0);
    probe_out0  : OUT STD_LOGIC_VECTOR(127 DOWNTO 0);
    probe_out1  : OUT STD_LOGIC_VECTOR(127 DOWNTO 0);
    probe_out2  : OUT STD_LOGIC_VECTOR(0 DOWNTO 0)
  );
END COMPONENT;

COMPONENT function128
    Port ( 
            clk     : in    std_logic;
            rst     : in    std_logic;
            done    : out   std_logic;		
            x       : in    STD_LOGIC_VECTOR (127 downto 0);
            y       : in    STD_LOGIC_VECTOR (127 downto 0);
            z       : out   STD_LOGIC_VECTOR (127 downto 0));
end COMPONENT;

signal probe_in0    : STD_LOGIC_VECTOR(127 DOWNTO 0);
signal probe_in1    : STD_LOGIC;
signal probe_out0   : STD_LOGIC_VECTOR(127 DOWNTO 0);
signal probe_out1   : STD_LOGIC_VECTOR(127 DOWNTO 0);
signal probe_out2   : STD_LOGIC;

begin

 inst_vio_test : vio_test
  PORT MAP (
    clk                 => clk,
    probe_in0           => probe_in0,
    probe_in1(0)        => probe_in1,
    probe_out0          => probe_out0,
    probe_out1          => probe_out1,
    probe_out2(0)       => probe_out2
  );
  
 inst_function128 : function128
    PORT MAP (
        clk     => clk,
        rst     => probe_out2,
        done    => probe_in1,    
        x       => probe_out0,
        y       => probe_out1,
        z       => probe_in0        
    );
    
end Behavioral;
