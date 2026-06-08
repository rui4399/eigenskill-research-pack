# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 232 / 500 | 0.4640 | 9.7516 | 0.194052 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_2000` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2001` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2002` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2003` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2004` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2005` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2006` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2008` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2009` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2011` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2012` | `mcq` | false | `B` | `A. high.` |
| baseline | `mmlu_2013` | `mcq` | false | `A` | `B. upper surface of the conductor.` |
| baseline | `mmlu_2014` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_2015` | `mcq` | false | `D` | `B. Microphone` |
| baseline | `mmlu_2016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2017` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2018` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2019` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2020` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2021` | `mcq` | true | `B` | `B. clean.` |
| baseline | `mmlu_2022` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2023` | `mcq` | true | `D` | `D. Flux.` |
| baseline | `mmlu_2024` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2025` | `mcq` | false | `D` | `C. RLC circuit.` |
| baseline | `mmlu_2026` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2027` | `mcq` | true | `B` | `B. Analog quantity` |
| baseline | `mmlu_2028` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2029` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2030` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2031` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2032` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2033` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2034` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2035` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2036` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2037` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2038` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2039` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2040` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2041` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2042` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2043` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2044` | `mcq` | true | `B` | `B. non linearly.` |
| baseline | `mmlu_2045` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2046` | `mcq` | true | `B` | `B. 80π coulombs.` |
| baseline | `mmlu_2047` | `mcq` | false | `A` | `B. MSB, Most Significant Bit` |
| baseline | `mmlu_2048` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2049` | `mcq` | false | `B` | `A. 3.33% .` |
| baseline | `mmlu_2050` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2051` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2052` | `mcq` | true | `C` | `C. both A and B.` |
| baseline | `mmlu_2053` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2054` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2055` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2056` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2057` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2058` | `mcq` | false | `A` | `D. No think` |
| baseline | `mmlu_2059` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2060` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2061` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2062` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2063` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2064` | `mcq` | false | `A` | `D. none of above.` |
| baseline | `mmlu_2065` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2066` | `mcq` | true | `C` | `C. 8` |
| baseline | `mmlu_2067` | `mcq` | true | `D` | `D. 5` |
| baseline | `mmlu_2068` | `mcq` | false | `B` | `C. 6` |
| baseline | `mmlu_2069` | `mcq` | true | `B` | `B. 4t = 112; $28` |
| baseline | `mmlu_2070` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2071` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2072` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2073` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2074` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2075` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2076` | `mcq` | false | `D` | `C. 1` |
| baseline | `mmlu_2077` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2078` | `mcq` | true | `A` | `A. 6` |
| baseline | `mmlu_2079` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2080` | `mcq` | true | `B` | `B. 14 minutes` |
| baseline | `mmlu_2081` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2082` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2083` | `mcq` | false | `D` | `C. 50` |
| baseline | `mmlu_2084` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2085` | `mcq` | false | `C` | `A. -12` |
| baseline | `mmlu_2086` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2087` | `mcq` | true | `A` | `A. -7` |
| baseline | `mmlu_2088` | `mcq` | false | `C` | `B. 63` |
| baseline | `mmlu_2089` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2090` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2091` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2092` | `mcq` | false | `D` | `C. 578` |
| baseline | `mmlu_2093` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2094` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2095` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2096` | `mcq` | false | `B` | `C. 16 remainder 5` |
| baseline | `mmlu_2097` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2098` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2099` | `mcq` | false | `D` | `B. 770 parts` |
| baseline | `mmlu_2100` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2101` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2102` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2103` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2104` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_2105` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2106` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2108` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2109` | `mcq` | false | `D` | `A. 15, 17` |
| baseline | `mmlu_2110` | `mcq` | true | `B` | `B. 12 cans` |
| baseline | `mmlu_2111` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2112` | `mcq` | false | `C` | `B. 11` |
| baseline | `mmlu_2113` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2114` | `mcq` | true | `D` | `D. -45` |
| baseline | `mmlu_2115` | `mcq` | false | `A` | `B. 40 birds` |
| baseline | `mmlu_2116` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2117` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2118` | `mcq` | true | `A` | `A. 120 miles` |
| baseline | `mmlu_2119` | `mcq` | true | `B` | `B. divide both sides by 6` |
| baseline | `mmlu_2120` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2121` | `mcq` | false | `D` | `C. 84 - t = 11; 73°F` |
| baseline | `mmlu_2122` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2123` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2124` | `mcq` | true | `B` | `B. 20` |
| baseline | `mmlu_2125` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2126` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_2127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2128` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2129` | `mcq` | false | `D` | `A. -4` |
| baseline | `mmlu_2130` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2131` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2132` | `mcq` | false | `A` | `C. 48` |
| baseline | `mmlu_2133` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2134` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2135` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2136` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2137` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2138` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2139` | `mcq` | true | `B` | `B. $6,049` |
| baseline | `mmlu_2140` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2141` | `mcq` | true | `A` | `A. $2.82` |
| baseline | `mmlu_2142` | `mcq` | true | `D` | `D. 5 over 6` |
| baseline | `mmlu_2143` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2144` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2145` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2146` | `mcq` | false | `A` | `C. -1` |
| baseline | `mmlu_2147` | `mcq` | false | `D` | `B. 4` |
| baseline | `mmlu_2148` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2149` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2150` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2151` | `mcq` | false | `A` | `B. 8.9` |
| baseline | `mmlu_2152` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2153` | `mcq` | true | `B` | `B. 66.5 seconds` |
| baseline | `mmlu_2154` | `mcq` | false | `B` | `D. 96` |
| baseline | `mmlu_2155` | `mcq` | true | `C` | `C. 180` |
| baseline | `mmlu_2156` | `mcq` | false | `A` | `C. 4:01` |
| baseline | `mmlu_2157` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2158` | `mcq` | true | `A` | `A. 48` |
| baseline | `mmlu_2159` | `mcq` | false | `C` | `B. 21` |
| baseline | `mmlu_2160` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2161` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2162` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2163` | `mcq` | false | `A` | `C. 2.61` |
| baseline | `mmlu_2164` | `mcq` | false | `C` | `B. 3.6` |
| baseline | `mmlu_2165` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2166` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2167` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2168` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2169` | `mcq` | false | `A` | `B. 2,400` |
| baseline | `mmlu_2170` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2171` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2172` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2173` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2174` | `mcq` | true | `B` | `B. subtract 20 from 180` |
| baseline | `mmlu_2175` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2176` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2177` | `mcq` | false | `B` | `C. 72` |
| baseline | `mmlu_2178` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2179` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2180` | `mcq` | false | `D` | `A. 6` |
| baseline | `mmlu_2181` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2182` | `mcq` | true | `B` | `B. 2.5` |
| baseline | `mmlu_2183` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2184` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2185` | `mcq` | false | `B` | `A. $1.40` |
| baseline | `mmlu_2186` | `mcq` | false | `A` | `C. 1,000` |
| baseline | `mmlu_2187` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2188` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2189` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2190` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2191` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2192` | `mcq` | true | `C` | `C. 9` |
| baseline | `mmlu_2193` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2194` | `mcq` | false | `D` | `C. 19,612` |
| baseline | `mmlu_2195` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2196` | `mcq` | false | `D` | `C. 72 km/h` |
| baseline | `mmlu_2197` | `mcq` | true | `B` | `B. 25 meters` |
| baseline | `mmlu_2198` | `mcq` | true | `C` | `C. 130 minutes` |
| baseline | `mmlu_2199` | `mcq` | false | `C` | `B. 144` |
| baseline | `mmlu_2200` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2201` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2202` | `mcq` | false | `D` | `C. 17` |
| baseline | `mmlu_2203` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2204` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2205` | `mcq` | true | `D` | `D. 120` |
| baseline | `mmlu_2206` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2207` | `mcq` | false | `D` | `B. 3` |
| baseline | `mmlu_2208` | `mcq` | true | `A` | `A. 3:58 p.m.` |
| baseline | `mmlu_2209` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2210` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2211` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2212` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2213` | `mcq` | false | `C` | `B. 17` |
| baseline | `mmlu_2214` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2215` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2216` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2217` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2218` | `mcq` | false | `C` | `B. conducting the survey at all shoe stores` |
| baseline | `mmlu_2219` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2220` | `mcq` | false | `D` | `C. 24 students` |
| baseline | `mmlu_2221` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2222` | `mcq` | false | `A` | `B. 9 stickers` |
| baseline | `mmlu_2223` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2224` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2225` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2226` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2227` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2228` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2229` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2231` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2232` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2233` | `mcq` | false | `C` | `B. 4 days` |
| baseline | `mmlu_2234` | `mcq` | true | `C` | `C. 18` |
| baseline | `mmlu_2235` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2236` | `mcq` | false | `A` | `B. -7` |
| baseline | `mmlu_2237` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2238` | `mcq` | false | `C` | `D. 79` |
| baseline | `mmlu_2239` | `mcq` | false | `A` | `C. -13` |
| baseline | `mmlu_2240` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2241` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2242` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2243` | `mcq` | false | `B` | `D. 20 over 28` |
| baseline | `mmlu_2244` | `mcq` | true | `A` | `A. -63` |
| baseline | `mmlu_2245` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2246` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2247` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2248` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2249` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2250` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2251` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2252` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2253` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2254` | `mcq` | true | `B` | `B. 15` |
| baseline | `mmlu_2255` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2256` | `mcq` | true | `B` | `B. -49°C` |
| baseline | `mmlu_2257` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2258` | `mcq` | false | `D` | `B. 27` |
| baseline | `mmlu_2259` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2260` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2261` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2262` | `mcq` | true | `B` | `B. 30/5` |
| baseline | `mmlu_2263` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2264` | `mcq` | true | `D` | `D. -1.1` |
| baseline | `mmlu_2265` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2266` | `mcq` | false | `C` | `B. 77` |
| baseline | `mmlu_2267` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2268` | `mcq` | true | `B` | `B. 18` |
| baseline | `mmlu_2269` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2270` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_2271` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2272` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2273` | `mcq` | false | `D` | `B. 29` |
| baseline | `mmlu_2274` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2275` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2276` | `mcq` | false | `C` | `B. 12 cm` |
| baseline | `mmlu_2277` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2278` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2279` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2280` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2281` | `mcq` | true | `B` | `B. $45` |
| baseline | `mmlu_2282` | `mcq` | false | `A` | `B. -7.4` |
| baseline | `mmlu_2283` | `mcq` | true | `B` | `B.ounces` |
| baseline | `mmlu_2284` | `mcq` | false | `C` | `B. $45 loss` |
| baseline | `mmlu_2285` | `mcq` | false | `B` | `C. 39` |
| baseline | `mmlu_2286` | `mcq` | false | `C` | `B. 2 subjects` |
| baseline | `mmlu_2287` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2288` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2289` | `mcq` | false | `C` | `B. 120` |
| baseline | `mmlu_2290` | `mcq` | true | `D` | `D. -36` |
| baseline | `mmlu_2291` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2292` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2293` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2294` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2295` | `mcq` | false | `B` | `C. 7:30 a.m.` |
| baseline | `mmlu_2296` | `mcq` | true | `C` | `C. $0.40` |
| baseline | `mmlu_2297` | `mcq` | false | `D` | `C. 2^3 • 3^2` |
| baseline | `mmlu_2298` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2299` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2300` | `mcq` | false | `D` | `B. 11 in.` |
| baseline | `mmlu_2301` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2302` | `mcq` | true | `A` | `A. 158` |
| baseline | `mmlu_2303` | `mcq` | false | `D` | `B. 1,801 R1` |
| baseline | `mmlu_2304` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2305` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2306` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2307` | `mcq` | true | `C` | `C. 5` |
| baseline | `mmlu_2308` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2309` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2311` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2312` | `mcq` | false | `A` | `B. 2 over 3` |
| baseline | `mmlu_2313` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2314` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2315` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2316` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2317` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2318` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2319` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2320` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2321` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2322` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2323` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2324` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2325` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2326` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2327` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2328` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2329` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2330` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2331` | `mcq` | false | `B` | `A. -85` |
| baseline | `mmlu_2332` | `mcq` | true | `C` | `C. 314` |
| baseline | `mmlu_2333` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2334` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2335` | `mcq` | true | `B` | `B. 260` |
| baseline | `mmlu_2336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2337` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2338` | `mcq` | true | `D` | `D. 180` |
| baseline | `mmlu_2339` | `mcq` | true | `B` | `B. $117.30` |
| baseline | `mmlu_2340` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2342` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2343` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2344` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2345` | `mcq` | true | `C` | `C. 94` |
| baseline | `mmlu_2346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2347` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2348` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2349` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2350` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2351` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2352` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2353` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2354` | `mcq` | false | `A` | `B. 2,400` |
| baseline | `mmlu_2355` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2356` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2357` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2359` | `mcq` | false | `D` | `B. 1.281` |
| baseline | `mmlu_2360` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2361` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2362` | `mcq` | true | `C` | `C. 400` |
| baseline | `mmlu_2363` | `mcq` | true | `B` | `B. 13` |
| baseline | `mmlu_2364` | `mcq` | true | `D` | `D. No mode` |
| baseline | `mmlu_2365` | `mcq` | true | `B` | `B. 136` |
| baseline | `mmlu_2366` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2367` | `mcq` | false | `C` | `B. $25.75` |
| baseline | `mmlu_2368` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2369` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2370` | `mcq` | true | `C` | `C. 4 over 9` |
| baseline | `mmlu_2371` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2372` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_2373` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2374` | `mcq` | false | `C` | `B. 495` |
| baseline | `mmlu_2375` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2376` | `mcq` | true | `D` | `D. 189 days` |
| baseline | `mmlu_2377` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2378` | `mcq` | true | `C` | `C. 9` |
| baseline | `mmlu_2379` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2380` | `mcq` | false | `C` | `B. 830` |
| baseline | `mmlu_2381` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2382` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2383` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2384` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2386` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2387` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2388` | `mcq` | true | `B` | `B. 43.3` |
| baseline | `mmlu_2389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2390` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2391` | `mcq` | false | `A` | `B. 74.18 m` |
| baseline | `mmlu_2392` | `mcq` | false | `D` | `B. 5-Mar` |
| baseline | `mmlu_2393` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2394` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2395` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2396` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2397` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2398` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2399` | `mcq` | false | `D` | `C. 20` |
| baseline | `mmlu_2400` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2402` | `mcq` | true | `C` | `C. 2 m` |
| baseline | `mmlu_2403` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2404` | `mcq` | false | `B` | `C. 62` |
| baseline | `mmlu_2405` | `mcq` | false | `C` | `B. $19.88` |
| baseline | `mmlu_2406` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2407` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_2408` | `mcq` | false | `A` | `D. 2-Jan` |
| baseline | `mmlu_2409` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2410` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2411` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2412` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2413` | `mcq` | false | `A` | `C. 110` |
| baseline | `mmlu_2414` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2415` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2416` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2417` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2418` | `mcq` | true | `C` | `C. 25 bouquets` |
| baseline | `mmlu_2419` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2420` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2421` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2422` | `mcq` | true | `B` | `B. 125` |
| baseline | `mmlu_2423` | `mcq` | true | `C` | `C. 48` |
| baseline | `mmlu_2424` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2425` | `mcq` | true | `C` | `C. 24` |
| baseline | `mmlu_2426` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2427` | `mcq` | false | `B` | `C. 8` |
| baseline | `mmlu_2428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2429` | `mcq` | false | `A` | `D. 1:09` |
| baseline | `mmlu_2430` | `mcq` | false | `C` | `D. 11 over 16` |
| baseline | `mmlu_2431` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2432` | `mcq` | true | `C` | `C. 11` |
| baseline | `mmlu_2433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2434` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2435` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2436` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2437` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2438` | `mcq` | false | `D` | `C. 120` |
| baseline | `mmlu_2439` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2440` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2441` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2442` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2443` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2444` | `mcq` | false | `A` | `B. Tcd` |
| baseline | `mmlu_2445` | `mcq` | false | `C` | `A. Some large houses are bigger than some apartments.` |
| baseline | `mmlu_2446` | `mcq` | false | `A` | `B. Invalid. Counterexample when G is true and H is false.` |
| baseline | `mmlu_2447` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2448` | `mcq` | false | `D` | `B. Every house is bigger than every apartment.` |
| baseline | `mmlu_2449` | `mcq` | false | `D` | `B. Invalid. Counterexample when K is true and L is false.` |
| baseline | `mmlu_2450` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2451` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2452` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2453` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2455` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2456` | `mcq` | false | `C` | `B. Invalid. Counterexample when E and F are true and G is false.` |
| baseline | `mmlu_2457` | `mcq` | false | `D` | `B. Invalid. Counterexample when H and I are true and J is false.` |
| baseline | `mmlu_2458` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2459` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_2460` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2461` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2462` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2463` | `mcq` | true | `B` | `B. Invalid. Counterexample when P and Q are true and R is false.` |
| baseline | `mmlu_2464` | `mcq` | true | `D` | `D. Mmsi` |
| baseline | `mmlu_2465` | `mcq` | true | `B` | `B. No apartment is bigger than any large house.` |
| baseline | `mmlu_2466` | `mcq` | false | `C` | `B. Invalid. Counterexample when J is true and K and L are false` |
| baseline | `mmlu_2467` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2468` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2470` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2472` | `mcq` | false | `A` | `B. Invalid. Counterexample when E and G are true and F is false.` |
| baseline | `mmlu_2473` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2474` | `mcq` | false | `A` | `B. Invalid. Counterexample when M is true and O and N are false` |
| baseline | `mmlu_2475` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2476` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2477` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2478` | `mcq` | false | `C` | `B. Invalid. Counterexample when P and Q are true and R and S are false` |
| baseline | `mmlu_2479` | `mcq` | true | `B` | `B. Invalid. Counterexample when T is true and W and U are false` |
| baseline | `mmlu_2480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2482` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2483` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2484` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2485` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2486` | `mcq` | false | `A` | `B. Contradictory` |
| baseline | `mmlu_2487` | `mcq` | false | `A` | `B. Invalid. Counterexample when T and X are true and U, W, and Z are false.` |
| baseline | `mmlu_2488` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2489` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2490` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2491` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2492` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2493` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2495` | `mcq` | false | `D` | `A. ~Bje` |
| baseline | `mmlu_2496` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2497` | `mcq` | true | `B` | `B. The Bees win their first game.` |
| baseline | `mmlu_2498` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2499` | `mcq` | true | `B` | `B. Contradictory` |
