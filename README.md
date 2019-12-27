# Introduction to the Quantum Bit

## Talk to be given at [PyCascades 2020](https://2020.pycascades.com)

## Coming soon
- Slidedeck
- Links for varying levels of explanations of superpositions and entanglements

## How to install IBM's Qiskit on your laptop

Official install doc: <https://qiskit.org/documentation/install.html>

Note: as recently as 28-Nov-2019, Qiskit did not work with Python 3.8. You can specify Python 3.7 by doing:
`$ conda create -n name_of_my_env python=3.7`

The basic procedure is (this does not replace the install doc above):
1. Install Anaconda
2. Create virtual environment using `conda create ...` and activate it.
3. Pip install qiskit
4. Start Anaconda, or restart if already running.
5. In Anaconda, select your virtual env.
6. Within Anaconda, install Jupyter Notebook - will install into your selected virtual env. (JupyterLab **may** also work.)
7. Launch Jupyter Notebook

## Resources (in work) (make outline of talk and place these within it?)

The famous EPR paper:<br/>
[Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?](https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777)<br/>
A. Einstein, B. Podolsky, and N. Rosen<br/>
Phys. Rev. 47, 777 – Published 15 May 1935

Bohr's response:<br/>
[Can Quantum-Mechanical Description of Physical Reality be Considered Complete?](https://journals.aps.org/pr/abstract/10.1103/PhysRev.48.696)<br/>
N. Bohr<br/>
Phys. Rev. 48, 696 – Published 15 October 1935

Corrected user guide page (can link to real IBM HTML page after PR is merged):<br/>
Shows math and quantum score for Bell test demo:<br/>
[Entanglement_and_Bell_Tests](https://github.com/brandonwarren/iqx-user-guide/blob/format/rst/full-user-guide/003-Multiple_Qubits_Gates_and_Entangled_States/002-Entanglement_and_Bell_Tests.rst)

