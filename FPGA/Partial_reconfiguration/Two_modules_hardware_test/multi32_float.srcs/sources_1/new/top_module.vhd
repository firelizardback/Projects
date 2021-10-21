library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity top_module is
    Port ( clk : in STD_LOGIC);
end top_module;

architecture Behavioral of top_module is

COMPONENT vio_0
  PORT (
    clk         : IN    STD_LOGIC;
    probe_in0   : IN    STD_LOGIC_VECTOR(127 DOWNTO 0);
    probe_in1   : IN    STD_LOGIC_VECTOR(127 DOWNTO 0);
    probe_in2   : IN    STD_LOGIC_VECTOR(0 DOWNTO 0);
    probe_in3   : IN    STD_LOGIC_VECTOR(0 DOWNTO 0);
    probe_out0  : OUT   STD_LOGIC_VECTOR(127 DOWNTO 0);
    probe_out1  : OUT   STD_LOGIC_VECTOR(127 DOWNTO 0);
    probe_out2  : OUT   STD_LOGIC_VECTOR(0 DOWNTO 0)
  );
END COMPONENT;

COMPONENT multiplier_organised
    Port ( 
            clk     : in    STD_LOGIC;
            rst     : in    STD_LOGIC;
            done    : out   STD_LOGIC;		
            x       : in    STD_LOGIC_VECTOR (127 downto 0);
            y       : in    STD_LOGIC_VECTOR (127 downto 0);
            z       : out   STD_LOGIC_VECTOR (127 downto 0));
end COMPONENT;

COMPONENT aes_enc 
	port (
            clk     : in    STD_LOGIC;
            rst     : in    STD_LOGIC;
            done    : out   STD_LOGIC;		
            x       : in    STD_LOGIC_VECTOR (127 downto 0);
            y       : in    STD_LOGIC_VECTOR (127 downto 0);
            z       : out   STD_LOGIC_VECTOR (127 downto 0));
end COMPONENT;

signal z_aes_in        : STD_LOGIC_VECTOR(127 DOWNTO 0);
signal z_mult_in       : STD_LOGIC_VECTOR(127 DOWNTO 0);
signal done_aes_in     : STD_LOGIC;
signal done_mult_in    : STD_LOGIC;
signal x_in            : STD_LOGIC_VECTOR(127 DOWNTO 0);
signal y_in            : STD_LOGIC_VECTOR(127 DOWNTO 0);
signal rst_in          : STD_LOGIC;

begin

vio_test : vio_0
  PORT MAP (
    clk                 => clk,
    probe_in0           => z_aes_in,
    probe_in1           => z_mult_in,
    probe_in2(0)        => done_aes_in, 
    probe_in3(0)        => done_mult_in, 
    probe_out0          => x_in,
    probe_out1          => y_in,
    probe_out2(0)       => rst_in
  );
  
 mult : multiplier_organised
    PORT MAP (
        clk     => clk,
        rst     => rst_in,
        done    => done_mult_in,    
        x       => x_in,
        y       => y_in,
        z       => z_mult_in        
    );
    
 aes : aes_enc
    PORT MAP (
        clk     => clk,
        rst     => rst_in,
        done    => done_aes_in,    
        x       => x_in,
        y       => y_in,
        z       => z_aes_in        
    );    
  
end Behavioral;