╔════════════════════════╗
║ ExHentai下載器 V0.1    ║
║ 作者：Yorutsuki        ║
╚════════════════════════╝

一、使用說明：

0. 開啟EXHentaiDLer.exe檔案即可開始程式。

1. 登入

1.1. 若userdata.txt沒有資料，會要求輸入cookies，會列出下列文字，並依照欄位填入。
> No cookies yet, please input them.
> ipb_member_id: 
> ipb_pass_hash: 
> igneous: 
輸入完後會進行嘗試登入。

1.2. 若userdata.txt含有資料，會詢問是否需要修改。
> Your cookies:
> ipb_member_id: xxxxxxx
> ipb_pass_hash: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
> igneous: xxxxxxxxx
> Do you want to change them(Y/N)?
輸入含有Y或y的文字會進行修改，輸入其餘文字則不修改，直接嘗試登入。
修改過程如同1.1.，在此不再敘述。

1.3. 登入成功會有Login Success字樣，登入失敗會要求重新輸入cookie。

2. 選擇資料夾，會有以下字樣。
> Input your folder path, start from "./"(local) or "C:/"(global) etc.
> Path:
若以"./"開頭則代表相對路徑，否則以絕對路徑。若輸入錯誤會造成直接閃退。
之後下載圖檔時，會在創建一個資料夾到該路徑底下。

3. 下載圖檔，會要求輸入網址。
> ExHentai URL: 
輸入完後開始進行下載，會有以下字樣。
> Get Data Success: (Folder Name) Pages: XX
> path: (Path)
> (1/XX)downloading (Path)/(Filename)
> download success
> (2/XX)downloading (Path)/(Filename)
> download success
...
...
下載結束後會顯示Done.，並詢問是否繼續。
> Done.
> Continue(Y/N)?
輸入含有N或n的文字會結束程式，輸入其餘文字則重複3.。

二、注意事項：

1. 此下載程式只能使用cookies登入。
2. userdata.txt會儲存輸入的cookies，勿刪除。
3. EXHentaiDLer.py是原始碼，不影響EXE檔執行。
4. 目前還沒有無登入下載e-hentai的功能。

三、著作聲明：

CC BY-NC