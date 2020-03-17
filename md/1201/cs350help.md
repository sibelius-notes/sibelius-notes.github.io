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

One more thing you need to do, which is also in `runprogram`, you need to activate the addr space. Remember `as_activate` doesn't activate anything. It's a terrible name.
What it does is to clear TLB. Cause we are changing the address space that this process is using, which means any TLB entries corresponding to previous address space, then
we need to clear old things.

Now we need to create stack. In `runprogram`, we just call `as_define_stack`. But over here, we need to do more work: pass all arguments to the new program by populating
the new program's stack with all args we have extracted from old programs. So my recommendation is to implement a new version `as_define_stack` that does both stack creation and copying arguments onto the stack for you.

Not only `execv` on this assign, go back and modify `runprogram` such that it can also take cmd line args.

And after your version of `as_define_stack`, it's safe to delete the old addr space. We don't delete it immediately since each of the steps can fail, and then you want to return error code from `execv`. Recall that it only returns calling program if it fails. If it succeeds then newprogram starts running.

Kernel also lives in the Virtual Memory and we are also going to destroy old addr. In kernel mode, we can directly access memeory in the user's addr space, but not safe. User program can do sth stupid, then the addr might be invalid. Kernel should NEVER trust the user address, so the safest: special function `copyin`/`copyout`: not just copy... but validate the addr first. Use `copyinstr`/`copyoutstr` when copying NULL terminated strings.

To copy
- `copyinstr`: copy the program into the kernel safely
- count \# of arguments: copy in each of the addresses of the array and checking how many do you have before NULL
- Then copy in each arg string

You need to allocate memory for pointer array and the strings, strings take memeory. You can use `strlen`, but remember it doesn't include NULL terminator. OR you could assume a total length &#92;(\le &#92;) 128 bytes.

We need to take all these args copied into the kernel, and put then onto the stack of new user program. But it's not sufficient to arbitrarily dump things. There are some conventions to dictate the things have to live on the stack so the new program knows where to find the parameters. True in OS/161 and modern OS. These arguments must go onto the stack with a particular byte alignment.

If you are storing an actual string on the stack, no alignment required, character can go anywhere at any kind of addr. But a pointer to a string must live at an addr that is divisible by 4. AND any other type must live at an addr divisible by 8. Macros: `args_size = ROUNDUP(args_size, 8);`.

You might notice I never talked about allocating any spaces for those args on stack, cuz you don't have to. When we create stack (`as_define_stack`), we already allocate whole memory for stack. You own the memory, don't need to malloc: calculate the address and write to it.

### Suggested Steps
1. Copy `runprogram` to `execv`, and make sure it compiles at least.
2. Copy the program name into `execv`, print it to the screen.
3. Do modification.<br>
Do not even attempt args part until you have it working. Arg passing is the hardest.
4. Count \# args, print to the screen.
5. Then copy str into the kernel, print to the screen.
6. Finally add the args to the stack.

> End of F19 Lec 15, 45:21

### A2b testing
```bash
sys161 kernel "p uw-testbin/hogparty;q"

sys161 kernel "p testbin/sty;q"

sys161 kernel "p uw-testbin/argtesttest;q"

sys161 kernel "p uw-testbin/argtest tests;q"

sys161 kernel "p testbin/add;q"
```


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
