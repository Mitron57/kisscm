## Задание 1
```bash
cat /etc/passwd | grep -o "^[^:]*" | sort
```

## Задание 2
```bash
cat /etc/protocols | awk '{print $2, $1}' | sort -nr | head -n 5
```

## Задание 3
```bash
#!/bin/bash
len=${#1}
str=$1
upper="-"
side="|"
printf "+"
printf "%0.s$upper" $(seq 1 $(expr $len + 2))
printf "+\n"
printf "$side $str $side\n"
printf "+"
printf "%0.s$upper" $(seq 1 $(expr $len + 2))
printf "+\n"
```

## Задание 4
```bash
grep -o -E '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | sort | uniq
```

## Задание 5
```bash
#!/bin/bash
 
chmod +x $1
sudo cp $1 /usr/local/bin
```
