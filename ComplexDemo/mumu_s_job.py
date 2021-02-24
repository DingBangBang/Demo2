#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def json_to_dict():
	j = '{"rateDetail":{"rateCount":{"total":18929,"shop":0,"picNum":7175,"used":1161},"rateDanceInfo":{"storeType":4,"currentMilles":1611767127306,"showChooseTopic":false,"intervalMilles":11498371120},"rateList":[{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2021-01-24 19:02:41","rateContent":"洗脸卸妆一步搞定，还养肤，很好用，新年礼盒，好看","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[{"coverUrl":"//img.alicdn.com/imgextra/i4/O1CN01tG9YBK1JQZpkH1ymM_!!0-tbbala.jpg","cloudVideoUrl":"//cloud.video.taobao.com/play/u/734765427a6f537263304931596f554e5a4d7a414a773d3d/p/1/d/hd/e/6/t/1/296326409408.mp4","feedId":0,"videoVoice":true,"videoId":296326409408,"flashUrl":"","status":1}],"displayUserLink":"","id":1119744460751,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/O1CN01FBbj1E1JQZpdeuBuX_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/O1CN01D8ymdD1JQZpe5Om8N_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/O1CN01GWpwrW1JQZpgssBXw_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":18,"hours":21,"seconds":43,"month":0,"timezoneOffset":-480,"year":121,"minutes":40,"time":1610977243000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"宇***1","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"111;G01;920-11-13,16;1424-12-0,8;920-11-22,24;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":24,"hours":19,"seconds":41,"month":0,"timezoneOffset":-480,"year":121,"minutes":2,"time":1611486161000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-24 11:55:14","rateContent":"琥珀一生推，超好用，皮肤屏障受损的超敏感肌使用感很好，卸的很快，质地不油腻，乳化也快，用完皮肤也不腻不紧绷，这次的价格比T3还便宜，无限回购了","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120511714260,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i2/O1CN01jDe2Zl260OMPaf7TO_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":24,"hours":11,"seconds":52,"month":0,"timezoneOffset":-480,"year":121,"minutes":51,"time":1611460312000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"g***9","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"5724-11-32,37;420-11-27,31;1224-11-43,53;1524-11-38,42;420-11-38,42;520-11-54,65;920-11-10,26;824-11-43,53;920-11-6,9;9224-11-10,26;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":24,"hours":11,"seconds":14,"month":0,"timezoneOffset":-480,"year":121,"minutes":55,"time":1611460514000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t1-18.png","rateDate":"2021-01-16 21:34:11","rateContent":"百香果来支持王一博啦，新年礼盒很喜庆，赠品也超级实在，啵啵明信片真的太帅啦，卸妆油也是超级好用无限回购，不油腻卸的干净。","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119240641954,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/O1CN01Szynz81GGYJboLTPw_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/O1CN01q8AAU61MpiPtZAbIc_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":16,"hours":21,"seconds":12,"month":0,"timezoneOffset":-480,"year":121,"minutes":32,"time":1610803932000,"day":6},"headExtraPic":"","aucNumId":0,"displayUserNick":"l***1","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,10;2524-11-52,59;920-11-19,26;1224-11-52,59;920-11-11,18;920-11-27,37;1424-11-38,51;50081009-11-38,51;50041002-11-52,59;50011005-11-11,18;50051014-11-52,59;50181000-11-19,26;","cmsSource":"天猫","tamllSweetLevel":1,"gmtCreateTime":{"date":16,"hours":21,"seconds":11,"month":0,"timezoneOffset":-480,"year":121,"minutes":34,"time":1610804051000,"day":6},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t4-18.png","rateDate":"2021-01-20 15:16:59","rateContent":"新年装太好看了！旅行装小瓶很方便，每次都送一堆可以的。秀家老司机了，以前是用完就买，现在是看中就买，谁让代言人好看呢！摩托姐姐博妈支持王一博！","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[{"coverUrl":"//img.alicdn.com/imgextra/i2/O1CN012g8t6k1SOaegXAWrH_!!2-tbbala.png","cloudVideoUrl":"//cloud.video.taobao.com/play/u/55796d575846512b6143476b57376c452b436e7257673d3d/p/1/d/hd/e/6/t/1/296367803235.mp4","feedId":0,"videoVoice":true,"videoId":296367803235,"flashUrl":"","status":1}],"displayUserLink":"","id":1120433619213,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":20,"hours":15,"seconds":33,"month":0,"timezoneOffset":-480,"year":121,"minutes":13,"time":1611126813000,"day":3},"headExtraPic":"","aucNumId":0,"displayUserNick":"一***1","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"111;920-11-17,26;920-11-0,7;920-11-50,58;920-11-8,16;920-11-59,70;","cmsSource":"天猫","tamllSweetLevel":4,"gmtCreateTime":{"date":20,"hours":15,"seconds":59,"month":0,"timezoneOffset":-480,"year":121,"minutes":16,"time":1611127019000,"day":3},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-23 08:21:47","rateContent":"非常喜欢，在有活动的时候入手，赠品很多 植村秀的卸妆油基本都用过了，紫色款和琥珀款值得回购，宝可梦和万里挑一的礼盒很喜欢。使用起来非常好乳化，用完很舒服，对敏感肌油痘肌也很友好，没有出现闭口闷痘的现象，味道也好闻，送的50毫升和试用装适合出差带出门。","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120732823761,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/O1CN0188pXeS1j7xkEk9Rcg_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/O1CN01BdE1bY1mz2UVuA0qu_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":18,"hours":0,"seconds":27,"month":0,"timezoneOffset":-480,"year":121,"minutes":40,"time":1610901627000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"一***得","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,4;1424-12-20,33;920-11-34,45;1524-11-61,70;920-12-15,19;920-11-46,60;124-11-101,106;920-11-107,124;10120-11-77,88;920-11-71,76;9224-11-77,88;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":23,"hours":8,"seconds":47,"month":0,"timezoneOffset":-480,"year":121,"minutes":21,"time":1611361307000,"day":6},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-20 21:23:33","rateContent":"跟evelom一样超级好用，关键比evelom方便，适合我这种懒人。外油内干的皮肤太合适了，终于不用纠结了。上一个出差时带的小瓶。","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[{"coverUrl":"//img.alicdn.com/imgextra/i4/O1CN01l6kau01xo0j7es6li_!!0-tbbala.jpg","cloudVideoUrl":"//cloud.video.taobao.com/play/u/6d386373564132677032744276747a77636d446365513d3d/p/1/d/hd/e/6/t/1/295507368866.mp4","feedId":0,"videoVoice":true,"videoId":295507368866,"flashUrl":"","status":1}],"displayUserLink":"","id":1120116418669,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":18,"hours":7,"seconds":35,"month":0,"timezoneOffset":-480,"year":121,"minutes":52,"time":1610927555000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"g***6","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-34,45;920-11-14,25;920-11-26,33;920-12-54,64;720-11-0,13;50151012-11-26,33;50041016-11-0,13;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":20,"hours":21,"seconds":33,"month":0,"timezoneOffset":-480,"year":121,"minutes":23,"time":1611149013000,"day":3},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t4-18.png","rateDate":"2021-01-19 16:46:13","rateContent":"比代购实惠多了 送了好几瓶中样儿的卸妆 包装很漂亮 符合马上过春节的气氛 让人看见很有仪式感 开心","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120331587117,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/O1CN01hvLs9y1Uzo4UcFdWx_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/O1CN01EfPUTh1aWqiw9ehbl_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":19,"hours":16,"seconds":20,"month":0,"timezoneOffset":-480,"year":121,"minutes":44,"time":1611045860000,"day":2},"headExtraPic":"","aucNumId":0,"displayUserNick":"妮***儿","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"820-12-8,19;920-11-47,49;220-11-20,25;920-11-26,36;50011005-11-0,49;","cmsSource":"天猫","tamllSweetLevel":4,"gmtCreateTime":{"date":19,"hours":16,"seconds":13,"month":0,"timezoneOffset":-480,"year":121,"minutes":46,"time":1611045973000,"day":2},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-21 22:54:24","rateContent":"回购这款卸妆油，很温和很好用。送的红扇子好喜庆啊，祝愿代言人王一博小朋友也红红火火，牛年大吉。","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120240282709,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/O1CN01kVCFQn1GL8H6dFc52_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i2/O1CN019VIhAq1OouxcIX2Ae_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":true,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":18,"hours":21,"seconds":13,"month":0,"timezoneOffset":-480,"year":121,"minutes":3,"time":1610974993000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"青***云","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"2324-11-8,14;1424-12-0,7;920-11-15,24;920-11-42,46;50041016-11-8,14;50111015-11-8,14;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":21,"hours":22,"seconds":24,"month":0,"timezoneOffset":-480,"year":121,"minutes":54,"time":1611240864000,"day":4},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2021-01-23 14:33:42","rateContent":"哇哦哇哦！没想到shu霸霸给我发的是礼盒装呢！喜欢，咱家洁颜油是真心好用，不但卸的干净还养肤，送了好多小样！谢谢霸霸！摩托姐姐支持代言人王一博~","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120779391498,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/O1CN018s1kCQ1jydID9O8Dw_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/O1CN01cYD6Pl1jydIGlyDye_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/O1CN01dFEo291jydIHGPyZg_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":23,"hours":14,"seconds":49,"month":0,"timezoneOffset":-480,"year":121,"minutes":31,"time":1611383509000,"day":6},"headExtraPic":"","aucNumId":0,"displayUserNick":"吖***羊","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"111;2524-11-37,46;920-11-59,71;920-11-26,36;920-11-23,25;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":23,"hours":14,"seconds":42,"month":0,"timezoneOffset":-480,"year":121,"minutes":33,"time":1611383622000,"day":6},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2021-01-17 10:44:24","rateContent":"好用，上脸不油腻，卸妆不刺激，而且干净，二次回购了","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120044195869,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/O1CN01uc0iZs296khrwP2K5_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":17,"hours":10,"seconds":9,"month":0,"timezoneOffset":-480,"year":121,"minutes":42,"time":1610851329000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"t***0","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,2;1424-11-9,14;2524-11-15,19;1224-11-3,8;50081009-11-20,25;50041016-11-0,2;50051014-11-3,8;50041002-11-9,14;50111062-11-15,19;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":17,"hours":10,"seconds":24,"month":0,"timezoneOffset":-480,"year":121,"minutes":44,"time":1610851464000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t2-18.png","rateDate":"2021-01-24 22:35:16","rateContent":"一直种草植村秀的卸妆油，试用后觉得是很温和的卸妆油，乳化效果也非常好！还送了很多赠品，棒！表白代言人王一博呀～","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120589054078,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/O1CN01bl2ul11QCZ1feVwC1_!!0-tmallfun.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":24,"hours":22,"seconds":28,"month":0,"timezoneOffset":-480,"year":121,"minutes":32,"time":1611498748000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"r***蕊","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-12-35,42;1524-11-26,34;1424-11-12,25;1424-12-0,11;920-11-43,44;","cmsSource":"天猫","tamllSweetLevel":2,"gmtCreateTime":{"date":24,"hours":22,"seconds":16,"month":0,"timezoneOffset":-480,"year":121,"minutes":35,"time":1611498916000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2021-01-22 12:25:23","rateContent":"温和度：很好不刺激 清爽度：洗完脸上很清爽没有油腻感 卸妆能力：卸得很干净 我的肤质：敏感混油皮","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119461172566,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/O1CN01vg2jBt1PkcrYVNpIM_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/O1CN01xMDs2f1YMCHUAvBdw_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":true,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":22,"hours":12,"seconds":30,"month":0,"timezoneOffset":-480,"year":121,"minutes":23,"time":1611289410000,"day":5},"headExtraPic":"","aucNumId":0,"displayUserNick":"t***7","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"G02;2324-12-0,3;2524-11-32,37;1224-11-14,26;2524-11-14,26;1424-12-27,31;2524-12-10,13;2324-11-4,9;9724-12-43,48;50111015-11-0,49;50051014-11-0,49;50041002-11-0,49;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":22,"hours":12,"seconds":23,"month":0,"timezoneOffset":-480,"year":121,"minutes":25,"time":1611289523000,"day":5},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-20 15:51:56","rateContent":"温和度：很棒 清爽度：很滋润的感觉 卸妆能力：真的牛 我的肤质：偏干","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119252904813,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/O1CN01ZYxPZv1VmoRuUsByR_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":17,"hours":9,"seconds":3,"month":0,"timezoneOffset":-480,"year":121,"minutes":22,"time":1610846523000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"x***7","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"1424-12-18,22;2524-12-7,10;2324-12-0,3;824-11-11,17;920-11-4,6;50111028-11-0,35;50041002-11-0,35;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":20,"hours":15,"seconds":56,"month":0,"timezoneOffset":-480,"year":121,"minutes":51,"time":1611129116000,"day":3},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-22 16:43:34","rateContent":"百香果支持王一博！祝王一博越来越好！ 这款卸妆油也真的很好用哦！","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119496464823,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/O1CN015jFHtb1QickT42qLe_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/O1CN01MY5xZF1QickY5tRtC_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":22,"hours":16,"seconds":29,"month":0,"timezoneOffset":-480,"year":121,"minutes":40,"time":1611304829000,"day":5},"headExtraPic":"","aucNumId":0,"displayUserNick":"1***0","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,8;1424-11-19,31;50041016-11-18,31;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":22,"hours":16,"seconds":34,"month":0,"timezoneOffset":-480,"year":121,"minutes":43,"time":1611305014000,"day":5},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"","rateDate":"2021-01-20 18:40:40","rateContent":"摩托姐姐为王一博而来，卸妆能力很强，非常温和～","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1120099554852,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i3/O1CN010EQ3Kc1LFhf2YsYiE_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":20,"hours":18,"seconds":34,"month":0,"timezoneOffset":-480,"year":121,"minutes":36,"time":1611138994000,"day":3},"headExtraPic":"","aucNumId":0,"displayUserNick":"泡***0","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"2324-11-18,22;1424-11-11,17;50041002-11-11,17;50111015-11-18,24;","cmsSource":"天猫","tamllSweetLevel":0,"gmtCreateTime":{"date":20,"hours":18,"seconds":40,"month":0,"timezoneOffset":-480,"year":121,"minutes":40,"time":1611139240000,"day":3},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t4-18.png","rateDate":"2021-01-17 13:38:27","rateContent":"很多礼品，十分惊喜！","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[{"coverUrl":"//img.alicdn.com/imgextra/i1/O1CN01vseSle1izicCpCvOB_!!2-tbbala.png","cloudVideoUrl":"//cloud.video.taobao.com/play/u/6c6557716268616a6e4d76364452765367706a2b59773d3d/p/1/d/hd/e/6/t/1/295062028758.mp4","feedId":0,"videoVoice":true,"videoId":295062028758,"flashUrl":"","status":1}],"displayUserLink":"","id":1119705902984,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/O1CN01QltXpW1LHzdgDbkWN_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":17,"hours":13,"seconds":5,"month":0,"timezoneOffset":-480,"year":121,"minutes":36,"time":1610861765000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"小***追","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"G02;820-11-0,4;920-11-5,9;","cmsSource":"天猫","tamllSweetLevel":4,"gmtCreateTime":{"date":17,"hours":13,"seconds":27,"month":0,"timezoneOffset":-480,"year":121,"minutes":38,"time":1610861907000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-19 07:52:50","rateContent":"卸妆干净，不紧绷，保湿不伤皮肤。当然也支持王一博代言。✌","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119080708420,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":19,"hours":7,"seconds":42,"month":0,"timezoneOffset":-480,"year":121,"minutes":51,"time":1611013902000,"day":2},"headExtraPic":"","aucNumId":0,"displayUserNick":"晴***颉","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"1424-11-0,4;920-11-16,26;2324-11-9,15;824-11-9,15;824-11-5,8;50111073-11-9,15;50111062-11-0,4;50111004-11-5,8;50031025-11-9,15;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":19,"hours":7,"seconds":50,"month":0,"timezoneOffset":-480,"year":121,"minutes":52,"time":1611013970000,"day":2},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-19 10:27:44","rateContent":"摩托姐姐支持王一博 温和度：完全没有刺激，很舒服 清爽度：卸完整张脸不油也不干，非常清爽 卸妆能力：卸得非常干净，卸完后不需要再用洗面奶，但一定要记得乳化这个步骤哦 我的肤质：混合","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119918542900,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i1/O1CN01Cmew641x6xUp63hy5_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i4/O1CN015bCiHF1x6xUpIIn5n_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i1/O1CN01syECA51x6xUshtcN6_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:450ml","anony":false,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":19,"hours":9,"seconds":14,"month":0,"timezoneOffset":-480,"year":121,"minutes":42,"time":1611020534000,"day":2},"headExtraPic":"","aucNumId":0,"displayUserNick":"飘***9","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,9;2324-12-10,13;2324-11-14,20;824-11-29,39;1424-12-45,49;2524-11-50,56;1224-11-29,39;1524-11-69,82;920-11-21,24;2524-12-25,28;2524-11-40,44;50041002-11-40,56;50031033-11-21,39;50111035-11-21,39;50111015-11-0,20;50051014-11-40,56;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":19,"hours":10,"seconds":44,"month":0,"timezoneOffset":-480,"year":121,"minutes":27,"time":1611023264000,"day":2},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t3-18.png","rateDate":"2021-01-24 13:50:40","rateContent":"摩托姐姐支持王一博，明信片好nice 非常好用，很温和，会一直回购","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119702592599,"aliMallSeller":false,"reply":"","pics":["//img.alicdn.com/bao/uploaded/i4/O1CN01EDPGWM29Ygrovm8Cu_!!0-rate.jpg","//img.alicdn.com/bao/uploaded/i3/O1CN01xZIn9Z29Ygrsm2aoQ_!!0-rate.jpg"],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":false,"displayUserNumId":0,"goldUser":true,"attributesMap":null,"tradeEndTime":{"date":24,"hours":13,"seconds":16,"month":0,"timezoneOffset":-480,"year":121,"minutes":49,"time":1611467356000,"day":0},"headExtraPic":"","aucNumId":0,"displayUserNick":"糖***喵","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-0,9;920-11-19,23;2324-11-24,27;920-11-10,18;","cmsSource":"天猫","tamllSweetLevel":3,"gmtCreateTime":{"date":24,"hours":13,"seconds":40,"month":0,"timezoneOffset":-480,"year":121,"minutes":50,"time":1611467440000,"day":0},"useful":true,"displayUserRateLink":""},{"auctionPicUrl":"","userInfo":"","displayRatePic":"","dsr":0,"displayRateSum":0,"appendComment":null,"fromMemory":0,"picsSmall":[],"tmallSweetPic":"tmall-grade-t2-18.png","rateDate":"2021-01-21 13:09:57","rateContent":"温和度：温和，卸妆干净，不油腻。王一博推荐的不错。🐱","fromMall":true,"userIdEncryption":"","sellerId":2820842454,"videoList":[],"displayUserLink":"","id":1119348316893,"aliMallSeller":false,"reply":"","pics":[],"buyCount":0,"userVipLevel":0,"auctionSku":"化妆品净含量:150ml","anony":true,"displayUserNumId":0,"goldUser":false,"attributesMap":null,"tradeEndTime":{"date":18,"hours":9,"seconds":4,"month":0,"timezoneOffset":-480,"year":121,"minutes":35,"time":1610933704000,"day":1},"headExtraPic":"","aucNumId":0,"displayUserNick":"可***0","structuredRateList":[],"carServiceLocation":"","userVipPic":"","serviceRateContent":"","memberIcon":"","attributes":"","position":"920-11-16,24;2324-12-0,3;1224-11-12,15;2324-11-4,6;1424-11-7,11;50111015-11-0,6;50041002-11-7,11;50051014-11-12,15;","cmsSource":"天猫","tamllSweetLevel":2,"gmtCreateTime":{"date":21,"hours":13,"seconds":57,"month":0,"timezoneOffset":-480,"year":121,"minutes":9,"time":1611205797000,"day":4},"useful":true,"displayUserRateLink":""}],"searchinfo":"","from":"search","paginator":{"lastPage":99,"page":1,"items":18289},"tags":[]}}'
	dic = json.loads(s=j)
	if "rateDetail" in dic:
		print('hi')
		for (i) in dic.get("rateDetail").items():
			if "rateList" in i:
				for (j) in i:
					if str(type(j)) == "<class 'list'>":
						for (list_item) in j:
							print(list_item.get('rateContent'))
	# for (k,v) in  dic.items():
	#     for(i,j) in v.items():
	#         #print (=="<class 'dict'>")
	#         if str(type(j))=="<class 'dict'>" :
	#                 print(j)


if __name__ == '__main__':
	json_to_dict()