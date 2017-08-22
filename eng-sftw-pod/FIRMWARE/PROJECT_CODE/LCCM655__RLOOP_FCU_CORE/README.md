## Turning `define` C Macros into a Python list (Python object) for `fcu_core__defines.h` in `eng-software-pod/FIRMWARE/PROJECT_CODE/LCCM655__RLOOP__FCU_CORE`  

`fcu_core__defines.h` has *flight control code constants.*    

### to generate a Python list that you import

In the directory of `eng-software-pod/FIRMWARE/PROJECT_CODE/LCCM655__RLOOP__FCU_CORE` which contains `fcu_core__defines.h`, do the following:

```
swig -python -module fcu_core__defines fcu_core__defines.i

gcc -c -fpic fcu_core__defines_wrap.c fcu_core__defines.h -I/usr/include/python2.7  

gcc -shared fcu_core__defines_wrap.o -o _fcu_core__defines.so
``` 

Then a Python list is generated and one can output and manipulate the values for the Flight control code constants.  Follow the jupyter notebook `fcu_core__defines.ipynb` for instructions.  

