socat pty,link=/dev/virtual1,raw tcp:$1:23&

python file.py