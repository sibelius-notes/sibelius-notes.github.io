---
title: CS 350 - Operating Systems (help page)
layout: mdtoc
---
... Also, check my [miscellaneous notes](../cs350/)
# Basics
## Installing and Configuring OS/161
From [*Installing OS/161 in the student.cs Computing Environment*](https://www.student.cs.uwaterloo.ca/~cs350/common/Install161.html).

Previous steps...
- Step 0: Which Machine to Use?
- Step 1: Setting Up Your Environment
- Step 2: Obtain a Copy of the OS/161 Source Code

### Step 3: Configure OS/161 and Build the OS/161 Kernel

In `cs350-os161`,
```bash
cd os161-1.99
./configure --ostree=$HOME/cs350-os161/root --toolprefix=cs350-
cd kern/conf
./config ASST0
cd ../compile/ASST0
# only need to do configuration once.
bmake depend
bmake
bmake install
```
### Step 4: Build the OS/161 User-level Programs
user level, no need to do it every time, but to be safe...
```
cd $HOME/cs350-os161/os161-1.99
bmake
bmake install
```
> You could also make it simple: `bmake && bmake install`. The second cmd only run provided the first succeeded.

### Step 5: Try Running OS/161
```bash
cd $HOME/cs350-os161/root
cp /u/cs350/sys161/sys161.conf sys161.conf
```
Still, don't need to do it every time.

To run the os, `sys161 kernel-ASST0` or simply `sys161 kernel`.

### Submitting
In `cs350-os161` directory: `/u/cs350/bin/cs350_submit 0`.

## 350-gdb
Source: [Debugging with GDB](https://www.student.cs.uwaterloo.ca/~cs350/common/gdb.html)

Two windows open, and both in `root` dir. Note that you need to have one `ssh userid@linux...` and the other one `ssh -Y userid@linux...`. Otherwise you will get msg: `Connection refused`.

One window (main): `sys161 -w kernel`.

The other one (debugger): `cs350-gdb kernel` and then,
```bash
(gdb) dir ../os161-1.99/kern/compile/ASST0
(gdb) target remote unix:.sockets/gdb
```

Then in debugger window:
```bash
(gdb) break panic
(gdb) c
# type commands in main window
# Then it will break on panic msg
(gdb) where
(gdb) bt
(gdb) list
```


# "Useful" Scripts
## keep awake
Keep the connection to `linux.student.cs` environment.
```bash
#!/bin/bash
secs=0
while :
do
    s=$(( secs%60 ))
    m=$(( secs/60 ))
    echo -ne " \033[31m$m mins $s secs have passed\033[0m\033[0K\r"
    sleep 1
    : $((secs++))
done
```
Press `ctrl+c` or `ctrl+z` to terminate.

## 350 git
git version control. Better to store the credentials locally.
```bash
#!/bin/bash
echo -e "\033[31mEnter the commit message\033[0m"
printf "> "
read msg

echo -e "\033[31m************************\033[0m"

git add *
git commit --allow-empty -m "$msg"


git push -u origin master
```

## 350 find
Find a function/variable. Where is it defined?!?
```bash
#!/bin/bash
echo -e "\033[31mEnter the key word\033[0m"
printf "> "
read msg

grep -IR --exclude-dir=compile $msg
```
credit to Kevin Lancot on piazza.

# Assignments
## A2a
**Deadlock**

After `sys161 kernel`, the OS stucks at
```bash
sys161: System/161 release 1.99.06, compiled Aug 23 2013 10:23:34
# cursor blinking here...
```

Spinlocks are available in boot up before locks, probly use spinlock instead.

And take a look at `boot in startup/main.c`:
```c
void
boot(void)
{   ...
    ram_bootstrap();
    proc_bootstrap();
    thread_bootstrap();
    hardclock_bootstrap();
    vfs_bootstrap();
    ...
}
```

## A2b
Weird assignment numebering scheme here instead of 0 1 2 3 4, we go 0 1 2a 2b 3. There's a reason for that: used to be 0 1 2 3, and 5 sys call in A2,
but problem was the true CS fashion: leave it until last 12 hours...

`execv` is not going to change the process structure. We are going to change the program that the process acts: addr space, threads.

Takes two params, first: program you want to run; second: an array of pointers to string arguments. Null-terminated array.

Few lines of code. Most lines, you can copy and paste from elsewhere in the OS: `runprogram`. What does it do?
- open the program file `vfs_open`
- Once the program is open, create a new addrspace for that program. `as_create`. And then `curproc_create` which you might have seen when
I was talking about `fork`. Set addr space of current process. As you set the addr space, you need to load the program into the addr space.
- `load_elf` is the actual act of loading the program's binary info and copy it into the correct position. (`elf`: executable linkable format, probly seen in CS241).
It creates the code and data segment, NO stack segment.
- Creates the user stack using `as_define_stack`.
- Once you have done all that, you program is loaded and has addr space, and you call `enter_new_process`. 
You are going to pass the address of the stack and the value return from `load_elf` which is the enter point function
that is the address of the first instruction to execute in the new program.




# Random stuff
## Some good problems for midterm??
*Explain the difference between internal and external fragmentation.*

From [CSE451, University of Washington](https://courses.cs.washington.edu/courses/cse451/00sp/misc/quiz2sol.txt):

> Internal fragmentation is the wasted space within each allocated block
because of rounding up from the actual requested allocation to the
allocation granularity.  External fragmentation is the various free
spaced holes that are generated in either your memory or disk space.
External fragmented blocks are available for allocation, but may be
too small to be of any use.

So paging eliminates external frag., not internal frag.
