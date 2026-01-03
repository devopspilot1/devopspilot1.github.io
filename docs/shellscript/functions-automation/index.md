---
title: "Shell Scripting Functions & Automation"
date: 2024-07-01
---

# Shell Scripting Functions & Automation

← [Back to Shell Scripting Guide](../../shellscript/index.md)

[![Shellscript part-4](../../images/shellscript-part-4.png)](https://www.youtube.com/watch?v=NAm9xUOTubU)

### What is function ?

Function is used to group the set of commands/logic and it will be executed only if it is called

Mainly used for reusability purpose.

### Clone the shellscript git repo

```
ubuntu@test:~$ git clone https://github.com/vigneshsweekaran/shellscript
Cloning into 'shellscript'...
remote: Enumerating objects: 271, done.
remote: Counting objects: 100% (271/271), done.
remote: Compressing objects: 100% (200/200), done.
remote: Total 271 (delta 135), reused 189 (delta 67), pack-reused 0
Receiving objects: 100% (271/271), 31.86 KiB | 1.18 MiB/s, done.
Resolving deltas: 100% (135/135), done.
```

```
ubuntu@test:~$ cd shellscript/tutorials/part-4/
```

```
ubuntu@test:~/shellscript/tutorials/part-4$ ll
-rwxrwxr-x 1 ubuntu ubuntu  158 May 15 11:38 1-function.sh*
-rwxrwxr-x 1 ubuntu ubuntu  238 May 15 11:38 2-function-return.sh*
-rwxrwxr-x 1 ubuntu ubuntu  516 May 15 11:38 3-function-return-array.sh*
-rwxrwxr-x 1 ubuntu ubuntu  894 May 15 11:38 4-create-user.sh*
```

### Basic function

```
#!/bin/sh

# Function Definition
greeting() {
   echo "Hello $1"
}

# Calling the function
greeting "DevopsPilot"

greeting "Vignesh"

greeting "Shellscript"
```

Here we created a function named `greeting` This will not be executed by itself. You have to call the function by its name, then only it will be executed

You can pass the arguments to the function, if it is expected.

In the above, we are calling the function `greeting` and passing the argument `Vignesh` Eg: greeting "vignesh"

You can call the function many number of times with different arguments based on requirement

```
ubuntu@test:~/shellscript/tutorials/part-4$ ./1-function.sh 
Hello DevopsPilot
Hello Vignesh
Hello Shellscript
```

In the above output, you have seen three times the `echo` command was executed with different outputs since we called the function 3 times with different arguments

### How to return some data from function

```
#!/bin/sh

# Function Definition
addition() {
  num1=$1
  num2=$2

  output=$(( num1 + num2 ))

  return $output
}

# Calling the function
addition 20 5

# Capture the result returned by last command
result=$?

echo "The output is $result"
```

In some scenarios you want to return the output data from the function to the caller.

You have use the `return` keyword to return the data from the function Eg: return $output

`$output` is the data you want to return

To capture the returned data. After the function call, you have to use `$?` EG: result=$?

So the returned data is captured and stored to a variable

NOTE: A function can return only a number or string

```
ubuntu@test:~/shellscript/tutorials/part-4$ ./2-function-return.sh 
The output is 25
```

### How to return a array from function

```
ubuntu@test:~/shellscript/tutorials/part-4$ cat 3-function-return-array.sh 
#!/bin/bash

output=()

# Function Definition
calculate() {
  num1=$1
  num2=$2

  output_add=$(( num1 + num2 ))
  output_sub=$(( num1 - num2 ))
  output_multiply=$(( num1 * num2 ))
  output_division=$(( num1 / num2 ))

  output=("$output_add" "$output_sub" "$output_multiply" "$output_division")
}

# Calling the function
calculate 20 5

echo "The addition result is ${output[0]}"
echo "The subtraction result is ${output[1]}"
echo "The multiplication result is ${output[2]}"
echo "The division result is ${output[3]}"
```

Since you can return only number or string, array cannot be returned directly from the function.

In this case, you have to declare the empty array outside the function Eg: output=()

And the update the array inside the function once the data is ready

So you can directly access the array, once the function is executed. No need to return the data from function here

Once the function `calculate` is executed. We can directly access the `${output[0]}` to get the first data from the array

```
ubuntu@test:~/shellscript/tutorials/part-4$ ./3-function-return-array.sh 
The addition result is 25
The subtraction result is 15
The multiplication result is 100
The division result is 4
```

### How to create and delete the linux users using script

```
#!/bin/bash

users_list=(raghav mani manoj devops)
delete_users_list=(raghav)

# Checks whether user is present or not
check_user(){
  USER=$1

  id ${USER}
  return $?
}

# To create user
create_user(){
  USER=$1
  COMMENT="Managed by script"
  useradd -c "$COMMENT" $USER --create-home
  echo "Created user $USER successfully !!!"
}

# To delete users
delete_users(){
  echo "Deleting Users ..."

  for user in ${delete_users_list[@]};
  do
    check_user $user
    user_status=$?

    if [[ $user_status -eq 0 ]]
    then
      userdel -r $user
    else
      echo "The user ${user} doesn't exist !!!"
    fi
  done
}

# Creating users
echo "Creating Users ..."

for user in ${users_list[@]};
do
  check_user $user
  user_status=$?

  if [[ $user_status -ne 0 ]]
  then
    create_user $user
  else
    echo "The user ${user} already exist !!!"
  fi
done

# Deleting Users
# delete_users
```

First we create two array's `users_list` to store the list of news users to create and `delete_users_list` to store the list of existing users you want to delete

And we create 3 functions,

check\_user --> To check whether user is already existing or not

create\_user --> To create a new user

delete\_users --> To delete the users listed in `delete_users_list` array

The execution starts at the `echo "Creating Users ..."` and then `for user in ${users_list[@]};`

For gets the first user from `users_list` array and stores to `user` variable.

Then we call the `check_user` with argument as `user` to check whether user is present or not.

The `check_user` function runs the `id $users` command to check whether user is present or not.

If the user is present `$?` will give `0` if not it returns non-zero number

Then we passes the result from function to who called the function.

Next to the function call, you can use `$?` to capture the data returned from the function.

`$?` is used for many purposes, when we check `$?` after command execution it gives the status\_code of the command

If we check after the function call, it gives the function return data.

Here the function may return `0` or non-zero number and storing the data to `user_status` variable

If `user_status` is `0` the user is already present, then the `if` condition just prints `echo "The user ${user} already exist !!!"`

If `user_status` is non-zero number, it enters `if` condition and call the `create_user` function with argument `user` to create the new linux user.

The for loop continues and creates all users listed in `users_list` array

Next `# delete_users` function call line is commented, it will not call the `delete_users()` function

If you want to delete the users listed in `delete_users_list` array. Uncomment the function call line `delete_users`

So the `delete_users()` function will be called and it checks whether the user is present or not using `check_user()` function and deletes the user using `userdel` command

The for loop inside `delete_users()` function continues and delete all user listed in `delete_users_list` array

```
ubuntu@test:~/shellscript/tutorials/part-4$ sudo ./4-user-management.sh 
Creating Users ...
id: ‘raghav’: no such user
Created user raghav successfully !!!
id: ‘mani’: no such user
Created user mani successfully !!!
id: ‘manoj’: no such user
Created user manoj successfully !!!
id: ‘devops’: no such user
Created user devops successfully !!!
```
{% include-markdown "../../_partials/subscribe-guides.md" %}
