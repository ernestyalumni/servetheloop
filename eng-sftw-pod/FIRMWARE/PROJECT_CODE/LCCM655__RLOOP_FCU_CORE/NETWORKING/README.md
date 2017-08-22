# SWIG notes/basics

`%include` - `%include` directive to include library files

**This page was very helpful.  I successfully created a Python module for this.  Take note.**  
cf. [Wrapping C/C++ for Python using SWIG – Set 1](http://www.geeksforgeeks.org/wrapping-cc-python-using-swig-set-1/)

Also helpful: http://www.swig.org/Doc1.3/SWIG.html

## SWIG *interface* file; must be created

- **%module** specifies name of module we'll use in Python
- `%{ ... %}` block provides location to insert additional code such as C header files or additional C declaration into the generated wrapper code.  
- **%include** lets us include additional files like header files.  

e.g.
```   
/* file : gfg.i */
 
/* name of module to use*/
%module gfg
%{
    /* Every thing in this file is being copied in 
     wrapper file. We include the C header file necessary
     to compile the interface */
    #include "gfg.h"
 
    /* variable declaration*/
    double myvar;
%}
 
/* explicitly list functions and variables to be interfaced */
double myvar;
long long int fact(long long int n1);
int my_mod(int m, int n);
 
/* or if we want to interface all functions then we can simply
   include header file like this - 
   %include "gfg.h"
*/   
```   

Try either
```
$ swig -python gfg.i
```
i.e.
```    
swig -target_language interface_file.i  
```


```
$ gcc -c -fpic gfg_wrap.c gfg.c -I/usr/include/python2.7    
```    
where this will generate two object files
“gfg_wrap.o” and “gfg.o”. In above command –

    -fpic generate position-independent code (PIC) suitable for use in a shared library, if supported for the target machine. Such code accesses all constant addresses through a global offset table (GOT)

Note: If you get error something like “… ‘Python.h’ file not found” then following might be possible causes –

    You might not have ‘Python.h’ file or
    You are providing wrong location of ‘Python.h’ file to compiler

EY: 20170729 I found that you do
```
python-config --cflags  
```  
This will locate which Python you're using and where it's at on root.  

Now, at last, we have to link generated objects files together to create a shared object which is analogous to dll files in windows. Use the following command, this will generate a “_gfg.so” shared object file –

```   
$ gcc -shared gfg.o gfg_wrap.o -o _gfg.so
```   

Here's what I did:
```
swig -python fcu_core__net__packet_types.i

gcc -c -fpic fcu_core__net__packet_types_wrap.c fcu_core__net__packet_types.h -I/usr/include/python2.7

gcc -shared fcu_core__net__packet_types_wrap.o -o _packet_types.so  
```  

For
``` 
swig -python fcu_core__net__packet_types.i
```
`-python` flag tells you which programming language you want to do it in.  

I also tried, before, that command,
```
swig -python -module packet_types fcu_core__net__packet_types.h
```
but this gave me an error when compiling the wrap; it seems like the SWIG interface file is really needed.  Please, someone explain.

Before that,
```
swig -python fcu_core__net__packet_types.h
# before that
swig -builtin -python fcu_core__net__packet_types.i 
```

So finally, this was the correct, reproducible, procedure:
```  
swig -python -module packet_types fcu_core__net__packet_types.i

gcc -c -fpic fcu_core__net__packet_types_wrap.c fcu_core__net__packet_types.h -I/usr/include/python2.7

gcc -shared fcu_core__net__packet_types_wrap.o -o _packet_types.so  
```  


