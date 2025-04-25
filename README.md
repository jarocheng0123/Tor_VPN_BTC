<a href="https://www.baidu.com/" style="
  display: inline-flex;          /* 改用 flex 布局 */
  flex-direction: column;         /* 子元素垂直排列 */
  align-items: center;            /* 水平居中 */
  justify-content: center;        /* 垂直居中（可选，根据高度调整） */
  width: 80px;                    /* 固定宽度 */
  text-align: center;             /* 文字居中（冗余，flex 已控制） */
  padding: 0;                     /* 移除默认内边距，通过 flex 控制间距 */
">
  <img src="https://raw.githubusercontent.com/jarocheng0123/beginner_guide/refs/heads/main/png/GFW/baidu.png" 
       width="80" 
       style="
         display: block;           /* 保持块级 */
         margin: 0 0 5px;          /* 仅保留下方间距，覆盖 GitHub 的默认 margin */
         max-width: 100%;          /* 防止图片溢出 */
       ">
  <span style="
    font-size: 12px;              /* 字体大小 */
    line-height: 1.2;             /* 行高，避免文字折行时错位 */
    /* 以下为关键：强制覆盖 GitHub 可能的文字样式 */
    margin: 0;                    /* 清除默认 margin */
    padding: 0;                   /* 清除默认 padding */
  ">百度</span>
</a>