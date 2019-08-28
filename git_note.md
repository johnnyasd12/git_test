Git note
===


## Initialize

```git init```
- 初始化該 repository

```git config --global user.name <GitHub 帳號>```

```git config --global user.email <GitHub 信箱>```
- 讓系統知道你的 GitHub 帳號
- 也可以不要設 global，只在該 repository 作用，把 --global 刪掉即可
- ```git config --global --unset-all user.name``` 可以把所有 global 的 user.name 刪掉

```git config --global core.editor "'subl' --wait"```
- 在使用 git commit 時，會預設 sublime 為 message 編輯器
- --wait 是為了讓 git 等到編輯器 save 且關閉後才 commit
- 要使用 vim 為預設則只要 ```git config --global core.editor "vim"``` 即可

```git config --list```
- 查看當前 config 設定

## 基本操作

```git add ```
- 若file add完作修改，要再add一次!

```git commit -am "訊息"```
- 將所有未被 add **且曾經被 add 過的檔案** add 後 commit

```git rm --cached filename```
- 取消追蹤 file

```git rm -r --cached foldername```
- 取消追蹤 folder


```git reset HEAD-2```
- 不要被 reset 誤導
- 是 go to 的意思，前往兩個 commit 之前的狀態
- ```git reset HEAD``` 
    - 回到 HEAD 的狀態(?)，將 stage 清空?

```git diff```
- 是**目前檔案(尚未add)** 和上次 commit 之間的差距
- 可以指定檔案，使用 ```git diff <檔案名稱>``` 

```git log -10```
- 查看最近 10 筆 log

```gitk --all```
- GUI 看 branch 方便

```git stash```
- 如果有尚未 commit 的變更，又想切 branch，就可以用這樣的 command 來儲存目前的狀態

### Branch

```git branch```
- 查看 branch

```git branch <branch名稱>```
- 新增 branch

```git checkout <branch名稱>```
- 切換到該branch
- 視窗中的檔案也會變化

```git checkout -b <branch名稱>```
- 創建 branch，並且切換到該 branch

```git branch -d <branch名稱>```
- 刪除 branch

```git merge <branch名稱>```
- 將某 branch 合併到目前 branch

```git rebase```
- 將某一支 branch 基於另一支 branch 的內容合併起來
- 例如現在在 branch b1
    - git rebase master 會基於 master 目前最後一次 commit 內容再把 b1 commit 的內容加上去


## Remote 端

```git remote add origin remote網址```
- 本地端知道 remote 對應到遠端網址

```git push -u origin master```
- 可以拆解成 
```
git push origin master
git checkout master
git branch -u origin/master
```
- 參數 -u 等同於 --set-upstream，設定 upstream 可以**使分支開始追蹤指定的遠端分支**

```git remote -v```
- 查看遠端版本的來源

```git remote add <自訂分支名稱> <專案網址.git>```
- 如果是 fork 來的 project，可以加入**原始來源**的版本控制
- 例如 ```git remote add upstream https://github.com/Mindmapp/mindmapp.git```
- 之後 ```git pull upstream master``` 就會把**原始來源**的 master 給 pull 下來

```git pull origin <branch名稱>```
- 將 remote 的 change 更新到 local端
- 會自動 merge，因此可能要處理 conflict
- 在某branch上pull 下來會直接更動到目前 branch

```git push origin <branch名稱>```
- 將要修改的檔案 add commit 完之後，push 該分支到 remote
- **盡量不要 push master**，會覆蓋到 remote 的 master.

### Collaborator

1. 點進 GitHub ropo 右上角 setting，左側的 Collaborators，加入 該user 的 username
2. 該user git clone 該專案
3. 該user 開新的branch




# References

- [Git 教學(1) : Git 的基本使用](https://blog.gogojimmy.net/2012/01/17/how-to-use-git-1-git-basic/)
- [30 天精通 Git 版本控管](https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/README.md)
- [Git - 更新 fork 出來的 repository](https://dotblogs.com.tw/explooosion/2018/08/09/025208)







###### tags: `coding`