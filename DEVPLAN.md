# 开发计划
##2018-08-04
    - 组合的计算和获取，包括关注的组合以及所有的组合(done)
    - 每日数据的更新(done)
    - vpn的使用获取ticker数据(done)
##2018-08-07
    - futu软件定时删除日志(done)
    - 通达信数据的解析和验证(done)
    - 获取每天的tick信息，写入数据库(done)
##2018-08-12
    - 前复权价格的计算方法(done)
    - mac等，技术指标的实现(done)
    - 前复权价格的计算方法(done)
##2018-08-22
    - 平均股价的获取(done)
    - 涨跌停数据的获取(done)
##2018-08-24
    - 板块的分析数据的获取(done)
##2018-09-21
    - MAC和筹码分布的设计与实现(done)
    - KDJ的实现(done)
    - 股票还未上市，没有k线的处理(done)
##2018-10-10
    - 完成板块成庄的选股模型
        - 博弈K线的差(done)
        - 逆势大盘的程度(done)
        - 近邻筹码的密集程度(done)
    - 港股通持股(done)
    - 融资融券分析，分析融资融券的换手率(done)
    - MAC和筹码系统的实现(done)
##2018-11-01
    - 获取指数的成分股(done)
    - 沪深两市每天的成交状态(done)
##2018-11-12
    - animation的数据修改为从influxdb获取，而不是从redis中获取。
    - 股票的贡献点数的计算
    - 每周投资者增加数量的爬虫
    - 大宗交易爬虫
    - 行业流通市值
    - 基金数据分析爬虫
    - 沪港通，深港通资金流向。
    - 资金的每日成交来源（融资融券，港股通，基金，MSCI，十大股东等）
    - 增加30分钟线和60分钟线
    - 根据日线生成周线和月线
    - 自定义broker，使得broker可以计算每一只股票的收益情况，每一只股票的仓位和总体的仓位的区分。
    - 超跌反弹模型
    - 牛熊股比模型
    - KDJ放量买入模型
    - 一阳指战法的实现
    - 神经网络学习和实践
    - 板块组合的战法与实现
    - 天线宝宝战法的代码实现
    - 傍大款战法的代码与实现
    - 随机深林完成，学习领回归和laso
    - influxdb的写入过程中需要增加列名字
    - 失败的列表增加重试的功能
    - Linux代码的破解
    - AAA云的登陆和自动订阅开发
    - 富途股票突破限制的情况
    - 通达信数据获取失败后的处理
    - gevent和python多进程并发
    - 可转债的战法
    - ETF期权的策略研究
    - 期货的策略研究
    - cmysql.py删除db和table确保成功
    - 异步读写mysql
    - 爬虫数据爬取异常报警
##TODO
    - 需要将长城证券的broker修改为富途的broker的类型。
    - gearmand同步中需要增加更新时同步，删除时同步的功能。
    - 复盘应该包含的功能：
        - capital alalysis
            - marauder map, 板块和个股的活点地图
                - 潜龙状态
                - 见龙状态
                - 飞龙状态
                - 亢龙状态
            - 流动市值与总成交额
                - 流动市值分析
                - 总成交额
            - 成交额板块分析
                - 成交额板块排行
                - #成交额增量板块排行
                - #成交额减量板块排行
                - #涨幅排行
                - #跌幅排行
            - 指数点数贡献分析(not do now)
                - 按照个股排序
            - 成交额构成分析(not do now)
                - 融资融券资金
                - 沪港通资金
                - 涨停板资金
                - 基金仓位资金
                - 股票回购
                - 大宗交易
            - emotion alalysis
                - 大盘的情绪分析
        - plate alalysis
                - capital alalysis(not do now)
                    - 沪港通
                    - 融资融券
                    - 基金
                    - 回购
                    - 大宗
        - stock analysis
                - capital alalysis(not do now)
                    - 沪港通
                    - 融资融券
                    - 基金
                    - 回购
                    - 大宗交易
                - technical analysis
                    - chip alalysis
                       #逆势大盘
                       #90:3
                       #逆势飘红
                       #牛长熊短
                       #线上横盘
                       #博弈K线无量长阳
        - model running
            - model training
            - model evaluation 
            - model backtesting
            - model trading
