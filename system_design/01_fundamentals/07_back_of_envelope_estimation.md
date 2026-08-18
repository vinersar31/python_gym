# 🔢 Back-of-the-Envelope Estimation Cheat Sheet

## 1. Latency Numbers Every Engineer Should Know

```
L1 Cache Reference ........................... 0.5 ns
Branch Mispredict ............................ 5 ns
L2 Cache Reference ........................... 7 ns
Mutex Lock/Unlock ............................ 25 ns
Main Memory (RAM) Reference .................. 100 ns
Compress 1KB with Zstandard .................. 2,000 ns (2 µs)
Send 2KB over 1 Gbps Network ................. 20,000 ns (20 µs)
Read 1 MB Sequentially from Memory (RAM) ..... 250,000 ns (250 µs)
Round Trip within Same Datacenter ............ 500,000 ns (0.5 ms)
Read 1 MB Sequentially from NVMe SSD ......... 1,000,000 ns (1 ms)
Disk Seek (HDD) .............................. 10,000,000 ns (10 ms)
Read 1 MB Sequentially from HDD .............. 20,000,000 ns (20 ms)
Send Packet: CA to Netherlands to CA ........ 150,000,000 ns (150 ms)
```

---

## 2. Power of Two & Units of Data

| Power of 2 | Exact Value | Approx | Unit |
|---|---|---|---|
| $2^{10}$ | 1,024 | 1 Thousand ($10^3$) | 1 KB (Kilobyte) |
| $2^{20}$ | 1,048,576 | 1 Million ($10^6$) | 1 MB (Megabyte) |
| $2^{30}$ | 1,073,741,824 | 1 Billion ($10^9$) | 1 GB (Gigabyte) |
| $2^{40}$ | 1,099,511,627,776 | 1 Trillion ($10^{12}$) | 1 TB (Terabyte) |
| $2^{50}$ | 1,125,899,906,842,624 | 1 Quadrillion ($10^{15}$) | 1 PB (Petabyte) |

---

## 3. Quick Calculation Rules & Time Conversions

- **Seconds in a Day**: $24 \times 3600 \approx 86,400 \text{ s} \approx 10^5 \text{ s}$ (or $8.64 \times 10^4$).
- **QPS from Daily Active Users (DAU)**:
  $$\text{Daily Requests} = \text{DAU} \times \text{Average Requests per User}$$
  $$\text{Average QPS} = \frac{\text{Daily Requests}}{86,400} \approx \frac{\text{Daily Requests}}{10^5}$$
  $$\text{Peak QPS} \approx 2 \times \text{to } 3 \times \text{Average QPS}$$

### Example Calculation:
- **DAU**: 100 Million
- **Requests / User / Day**: 10 reads, 1 write
- **Read QPS**: $\frac{100\text{M} \times 10}{10^5} = \frac{10^9}{10^5} = 10,000 \text{ Read QPS}$
- **Peak Read QPS**: $2 \times 10,000 = 20,000 \text{ QPS}$
- **Daily Storage (if 1 write = 500 Bytes)**: $100\text{M} \times 500\text{ B} = 50 \text{ GB / day}$
- **5-Year Storage**: $50 \text{ GB} \times 365 \times 5 \approx 91.25 \text{ TB}$
