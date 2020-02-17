# Introduction to the Quantum Bit

## Talk given at [PyCascades 2020](https://2020.pycascades.com) <https://www.youtube.com/watch?v=9V7n1SUEl5g&t=5200>

## How to install IBM's Qiskit on your laptop

Official install doc: <https://qiskit.org/documentation/install.html>

Note: as recently as 28-Nov-2019, Qiskit did not work with Python 3.8. You can specify Python 3.7 by doing:<br>
`$ conda create -n name_of_my_env python=3.7`

The basic procedure is (this does not replace the install doc above):
1. Install Anaconda
2. Create virtual environment using `conda create ...` and activate it.
3. Pip install qiskit
4. Start Anaconda, or restart if already running.
5. In Anaconda, select your virtual env.
6. Within Anaconda, install Jupyter Notebook - will install into your selected virtual env. (JupyterLab **may** also work.)
7. Launch Jupyter Notebook

## Resources

IBM Quantum Computing Documentation & Support:<br>
<https://quantum-computing.ibm.com/support>

To see entanglement and Bell tests page:<br>
1. IBM Quantum Experience User Guide
2. Left pane: Entanglement and Bell Tests

Textbook and video series:<br>
<https://qiskit.org/education>

The famous EPR paper:<br>
[Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?](https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777)<br>
A. Einstein, B. Podolsky, and N. Rosen<br>
Phys. Rev. 47, 777 – Published 15 May 1935

Interactive Bloch sphere visualization tool:<br>
<https://javafxpert.github.io/grok-bloch/>

If there is anything missing that you hoped to find here, please let me know.


