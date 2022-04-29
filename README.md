<!-- 专门来进行代码格式化的文件，不重要 -->
<!-- github的markdown无法识别style标签 -->
<!--
    TODO:
    1.给README.me页面制作目录
    2.页面做重定向，让每次页面开始的位置是学习内容进行的位置
    3.加其他效果，待定
 -->
<!-- 不行，style还是没法被Github识别 -->
<!-- <style>
    .loading {
        background-color: yellow;
    }
</style> -->
<!-- 使用JavaScript重定向页面 -->
<!-- <script>
    window.onload = function () {
        setInterval("redirect();", 3000);
    }
    function redirect() {
        window.location.href = "index.html"
    }
</script> -->

<body>
    <h1>
        Python基础学习
    </h1>
    <h2>
        1. 环境搭建
    </h2>
    <a href="https://jhzxy4odk0.feishu.cn/wiki/wikcnO5QRv6AgqxG9w1n8oDpM3b" alt="Python云服务器环境">云服务器下Python环境使用</a>
    <h2>
        2. 主要学习内容
    </h2>
    <h3>
        2.1 起步
    </h3>
    <ol>
        <li>搭建变成环境</li>
        <li>在不同操作系统中搭建Python环境</li>
        <li>运行Hello world程序</li>
        <li>解决安装问题</li>
        <li>从终端中运行Python程序</li>
    </ol>
    <h3>
        2.2 变量和简单数据类型
    </h3>
    <ol>
        <li>运行hello_world.py</li>
        <li>认识变量</li>
        <li>认识字符串</li>
        <li>数</li>
        <li>注释</li>
        <li>Python之禅</li>
        <li>小结</li>
    </ol>
    <!-- 对于Markdown文件，如果用HTML语法来写的话，中间不能断 -->
    <h3>
        2.3 列表初探
    </h3>
    <ol>
        <li>列表是什么</li>
        <li>修改、添加、和删除列表中的元素
            <ul>
                <li>append()</li>
                <li>insert()</li>
                <li>del</li>
                <li>pop()</li>
                <li>remove()</li>
            </ul>
        </li>
        <li>组织列表
            <ul>
                <li>sort()</li>
                <li>sorted()</li>
                <li>reverse()</li>
                <li>len()</li>
            </ul>
        </li>
    </ol>
    <h3>
        2.4 列表操作
    </h3>
    <ol>
        <li>遍历列表
            <ul>
                <li>学习for in</li>
            </ul>
        </li>
        <li>缩进格式注意事项</li>
        <li>创建数值列表
            <ul>
                <li>range()</li>
                <li>min()</li>
                <li>max()</li>
                <li>sum()</li>
                <li>列表解析</li>
            </ul>
        </li>
        <li>使用列表的一部分
            <ul>
                <li>切片[:]</li>
                <li>遍历切片</li>
                <li>复制切片</li>
            </ul>
        </li>
        <li>元组
            <ul>
                <li>定义元组</li>
                <li>遍历元组</li>
                <li>修改元组变量</li>
            </ul>
        </li>
        <li>设置代码格式pep8</li>
    </ol>
    <h3>
        2.5 If语句
    </h3>
    <ol>
        <li>if简单示例</li>
    </ol>
    <!--
            这个是分界线，上面的是学习内容，下面的是相关资料
         -->
    <h2>
        3. 附录
    </h2>
    <h3>
        a. 相关资料
    </h3>
    <ul>
        <li><a href="https://jhzxy4odk0.feishu.cn/wiki/wikcnE1N2WdiLmx2wEsxq7MNXPh">《Python编程从入门到实践第2版》</a></li>
        <li><a href="https://jhzxy4odk0.feishu.cn/wiki/wikcnGiv1aZCqwMTNsdjnN5iqoe">《快快乐乐学Linux》</a></li>
        <li><a href="https://markdown.com.cn/basic-syntax/" alt="markdown的基本语法">&nbsp;&nbsp;Markdown基本语法</a></li>
    </ul>
    <h3>
        b. Jupyter Notebook in Visual studio Code 快捷键
    </h3>
    <ul>
        <li>shift+回车键：运行当前单元格的代码，并创建新的单元格</li>
        <li>Ctrl+回车键：运行当前的代码</li>
    </ul>
    <!--
        下面是测试部分
     -->
    <div style="width:150px;overflow: hidden;">
        <div id="title" style="height:30px;background-color: #FFE08B;" onclick="onTileClick()">标题</div>
        <div id="content" style="height:150px;background-color: #FFFAB9;transition: height 0.2s;">
            白日依山尽<br>
            黄河入海流<br>
            欲穷千里目<br>
            更上一层楼<br>
        </div>
    </div>
    <script type="text/javascript">
        var content = document.getElementById("content");
        function onTileClick() { content.style.height = content.offsetHeight === 150 ? 0 + 'px' : 150 + 'px'; }
    </script>
</body>
</html>