title: CS 350 - Operating Systems (help page)
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
## A2a - Deadlock
After `sys161 kernel`, the OS stucks at
```bash
sys161: System/161 release 1.99.06, compiled Aug 23 2013 10:23:34
# cursor blinking here...
```

**Q**: *Cannot acquire lock in proc_bootstrap*

**A**:
> Spinlocks are available in boot up before locks, so you might consider using a spinlock. If you are just doing something short (e.g. incrementing a count or initializing a value) in the OS, a spinlock actually would be more efficient.

and look at `boot in startup/main.c`:
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
Credit to Kevin Lancot on piazza.

**Q**: *Deadlock when initializing a spinlock*

**A** from *Anonymous Beaker*:
> I had the same issue; check the proc_bootstrap function and more specifically the order the different things are being initiated. For me, I couldn't use any protection before the kernel proc has been initiated. Hope this helps.
<br>
~ An instructor (Kevin Lanctot) endorsed this answer  ~

**A** from Kevin Lancot:
> 2) A work around, what I actually did, is to detect if you are in bootstrap (kproc is initialize early in proc_bootstrap) and avoid using the lock to assign a pid there because there is just one process at this point in time.
