# Git note

```git commit -am "訊息"```
- 將所有未被 add **且曾經被 add 過的檔案** add 後 commit

```git reset HEAD-2```
- 不要被 reset 誤導
- 是 go to 的意思，前往兩個 commit 之前的狀態
- ```git reset HEAD``` 
    - 回到 HEAD 的狀態(?)，將 stage 清空?

```git diff```
- 是**目前檔案(尚未add)** 和上次 commit 之間的差距

```git remote add origin remote網址```
- 本地端知道 remote 對應到遠端網址

```git push -u origin master```
- 可以拆解成 
```
git push origin master
git checkout master
git branch -u origin/master
```



```gitk --all```
- GUI 看 branch 方便

### Git Branch

```git branch```
- 查看 branch

```git branch br名稱```
- 新增 branch

```git checkout br名稱```
- 切換到該branch
- 視窗中的檔案也會變化

```git rebase```
- 將某一支 branch 基於另一支 branch 的內容合併起來
- 例如現在在 branch b1
    - git rebase master 會基於 master 目前最後一次 commit 內容再把 b1 commit 的內容加上去



















