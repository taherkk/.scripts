nc -l -p 5912 <fifo | nc 127.0.0.1 5901 >fifo
