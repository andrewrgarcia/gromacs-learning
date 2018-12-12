# Gromacs Free Energy of Solvation Tutorial

http://www.gromacs.org/Documentation/Tutorials/Free_energy_of_solvation_tutorial

Results in **RESULTS** file

---------------------------------------------------
Ethanol in Water (excerpt)

Temperature: 300 K

Detailed results in kT (see help for explanation):

DG == "Delta G"

lam_A|lam_B|DG|+/-|s_A|+/-|s_B|+/-|stdev|+/-
--- | --- | --- | --- | --- | --- | --- | --- | --- | ---
0|1|-8.14|0.07|0.24|0.04|0.23|0.04|0.73|0.02
1|2|-5.86|0.03|0.27|0.04|0.27|0.04|0.7|0.02
2|3|1.97|0.08|1.33|0.09|1.47|0.1|1.74|0.08
3|4|7.34|0.82|35.73|1.25|8.31|0.86|22.45|15.71
4|5|1.4|0.11|3.22|0.26|1.74|0.1|2.25|0.1
5|6|-3.71|0.4|14.96|0.86|11.29|0.64|11|0.43



Final results in kJ/mol:

point|DG|+/-
--- | --- | ---
point 0-1|-20.31|0.17
point 1-2|-14.63|0.08
point 2-3|4.92|0.21
point 3-4|18.3|2.05
point 4-5|3.49|0.28
point 5-6|-9.27|1
total 0-6|-17.49|2.06
