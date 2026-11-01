# C++ Socket Programming：TCP 與 UDP
[筆記](https://hackmd.io/@YongCheng/rkgiUNs3zl)

使用本機 `127.0.0.1:8080` 測試 Echo 服務：Client 傳送文字，Server 將原文回傳。

## 檔案說明

| 檔案 | 用途 |
|---|---|
| `tcpserver.cpp` | TCP Echo Server（接收訊息並原文回傳） |
| `tcpclient.cpp` | TCP Echo Client（傳送訊息並接收原文回覆） |
| `udpserver.cpp` | UDP Uppercase Server（接收小寫英文句子，轉成大寫後回傳） |
| `udpclient.cpp` | UDP Uppercase Client（傳送小寫英文句子並接收大寫結果） |

## 編譯前準備

確認已安裝 C++ 編譯器：

```bash
g++ --version
```

在終端機切換到上述四個檔案所在的資料夾，再執行編譯指令。

VS Code 可透過「終端機 → 新增終端機」開啟終端機。

## Windows：編譯

以下指令適用於 MinGW g++：

```powershell
g++ -std=c++17 -Wall -Wextra tcpserver.cpp -o tcpserver.exe -lws2_32
g++ -std=c++17 -Wall -Wextra tcpclient.cpp -o tcpclient.exe -lws2_32
g++ -std=c++17 -Wall -Wextra udpserver.cpp -o udpserver.exe -lws2_32
g++ -std=c++17 -Wall -Wextra udpclient.cpp -o udpclient.exe -lws2_32
```

## Windows：執行

開啟兩個 PowerShell 終端機，兩者都切換到執行檔所在的資料夾。

### TCP 測試

終端機 A：先啟動 Server。

```powershell
.\tcpserver.exe
```

終端機 B：啟動 Client。

```powershell
.\tcpclient.exe
```

### UDP 測試

終端機 A：先啟動 Server。

```powershell
.\udpserver.exe
```

終端機 B：啟動 Client。

```powershell
.\udpclient.exe
```

## macOS／Linux：編譯

```bash
g++ -std=c++17 -Wall -Wextra tcpserver.cpp -o tcpserver
g++ -std=c++17 -Wall -Wextra tcpclient.cpp -o tcpclient
g++ -std=c++17 -Wall -Wextra udpserver.cpp -o udpserver
g++ -std=c++17 -Wall -Wextra udpclient.cpp -o udpclient
```

macOS 的 `g++` 可能實際使用 Apple Clang，也能編譯本範例。

## macOS／Linux：執行

開啟兩個終端機，兩者都切換到執行檔所在的資料夾。

### TCP 測試

終端機 A：先啟動 Server。

```bash
./tcpserver
```

終端機 B：啟動 Client。

```bash
./tcpclient
```

### UDP 測試

終端機 A：先啟動 Server。

```bash
./udpserver
```

終端機 B：啟動 Client。

```bash
./udpclient
```

## 預期結果

### TCP

Server 啟動後顯示：

```text
TCP Server waiting...
```

Client 啟動後，輸入 `Hello socket`：

```text
Enter one line: Hello socket
Echo: Hello socket
```

Server 顯示：

```text
Received: Hello socket
```

### UDP

Server 啟動後顯示：

```text
UDP Server waiting...
```

Client 輸入 `hello socket`：

```text
Enter a lowercase sentenc: hello socket
Uppercase response: HELLO SOCKET
```

Server 顯示：

```text
Received: hello socket
Uppercase: HELLO SOCKET
```

## 編譯選項

| 選項 | 用途 |
|---|---|
| `-std=c++17` | 使用 C++17 |
| `-Wall` | 開啟一組常用警告 |
| `-Wextra` | 開啟額外警告 |
| `-o` | 指定輸出檔名 |
| `-lws2_32` | Windows 連結 Winsock 函式庫 |

macOS／Linux 不需要 `-lws2_32`。

## 使用注意事項

- 先啟動 Server，再啟動對應的 Client。
- TCP Client 必須搭配 TCP Server；UDP Client 必須搭配 UDP Server。
- `127.0.0.1` 代表自己的電腦，這份設定供本機測試。
- 每次輸入最多 1024 bytes，中文字可能占多個 bytes。
- 每個 Server 只處理一次訊息交換，再次測試前須重新啟動。
- TCP 使用換行 `\n` 作為訊息結束符號。
- UDP 沒有設定接收逾時與重傳；若收不到回覆，可能持續等待。
- 可按 `Ctrl + C` 結束等待中的程式。

## TCP Socket 互動網頁

網址：https://Yong-Cheng-Huang.github.io/socket-programming/

提供播放／暫停、上一步／下一步、拖曳進度與重播，共 20 個狀態；區分 listening socket 和 connected socket，顯示交握、資料傳送與關閉連線。

- `src/animation.html`：可直接閱讀與編輯的 HTML、CSS、JavaScript。步驟 label 保留 `margin-top:16px`。
- `index.html`：可直接開啟的完整網頁，內含動畫 iframe。
- `scripts/build.py`：將動畫原始碼重新嵌入網頁，輸出至 `_site/`。
- `.github/workflows/pages.yml`：推送網頁更新到 `main` 後自動部署 GitHub Pages。

修改 `src/animation.html` 後執行：

```bash
python3 scripts/build.py
python3 -m http.server 8000 --directory _site
```

在瀏覽器開啟 `http://localhost:8000` 預覽。提交並推送 `src/animation.html` 和重新產生的 `index.html` 即可更新網站。
