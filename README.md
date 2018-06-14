# intro
just use for alisoftsec;
use grep;
only support linux|macos
# usage
    python3 phcat.py -t target_directory -e c -l c
    
# rules
json文件
```json
{
  "author":"wh1t3P1g", //作者
  "name":"command execution", // 唯一的描述名
  "status":"on", // 是否开启规则
  "language":"c", // 表示语言 这里就写c吧
  "regex":"\\bsystem\\s*\\(|\\bexec[a-z]{0,2}\\s*\\(|\\bpopen\\s*\\("
  // 这边的正则为grep的正则
}
```


