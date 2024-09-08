## Задание 1
```bash
cat /etc/passwd | grep -o "^[^:]*" | sort
```
### Результат
![Результат задания 1](https://github.com/Mitron57/kisscm/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-02%20%D0%B2%2017.48.36.png)
## Задание 2
```bash
cat /etc/protocols | awk '{print $2, $1}' | sort -nr | head -n 5
```
### Результат
![Результат задания 2](https://github.com/Mitron57/kisscm/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-02%20%D0%B2%2017.50.00.png)
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
### Результат
![Результат задания 3](https://github.com/Mitron57/kisscm/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2000.11.19.png)

## Задание 4
```bash
grep -o -E '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | sort | uniq
```
### Результат
![Результат задания 4](https://github.com/Mitron57/kisscm/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2000.13.11.png)

## Задание 5
```bash
#!/bin/bash
 
chmod +x $1
sudo cp $1 /usr/local/bin
```
### Результат
![Результат задания 5](https://github.com/Mitron57/kisscm/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-09%20%D0%B2%2000.16.12.png)
