# ray-mlchain-benchmark
code used in benchmarking ray vs mlchain

1. mlchainreceiver.py is the mlchain server
2. mlchainsender.py is to send the data to the mlchain server for benchmarking mlchain performance
3. receiver.py is a flask server for benchmarking ray data transfer over the network performance
4. sender.py is to send the data to the flask server
5. rayset.py is to benchmark in-memory storage performance
6. testserialize.py is to benchmark pickle protocol 5 performance used in ray/pyarrow
7. network benchmark.xlsx is the benchmark result
