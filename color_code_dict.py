color_dict = {"000":"0","0A0":"1","010":"2","020":"3","030":"4","040":"5","050":"6","060":"7","070":"8","0X0":"9",\
"00A":"10","0AA":"11","01A":"12","02A":"13","03A":"14","04A":"15","05A":"16","06A":"17","07A":"18","0XA":"19",\
"002":"30","0A2":"31","012":"32","022":"33","032":"34","042":"35","052":"36","062":"37","072":"38","0X2":"39",\
"003":"40","0A3":"41","013":"42","023":"43","033":"44","043":"45","053":"46","063":"47","073":"48","0X3":"49",\
"004":"50","0A4":"51","014":"52","024":"53","034":"54","044":"55","054":"56","064":"57","074":"58","0X4":"59",\
"005":"60","0A5":"61","015":"62","025":"63","035":"64","045":"65","055":"66","065":"67","075":"68","0X5":"69",\
"006":"70","0A6":"71","016":"72","026":"73","036":"74","046":"75","056":"76","066":"77","076":"78","0X6":"79",\
"007":"80","0A7":"81","017":"82","027":"83","037":"84","047":"85","057":"86","067":"87","077":"88","0X7":"89",\
"00X":"90","0AX":"91","01X":"92","02X":"93","03X":"94","04X":"95","05X":"96","06X":"97","07X":"98","0XX":"99",\
"A00":"100","AA0":"101","A10":"102","A20":"103","A30":"104","A40":"105","A50":"106","A60":"107","A70":"108","AX0":"109",\
"A0A":"110","AAA":"111","A1A":"112","A2A":"113","A3A":"114","A4A":"115","A5A":"116","A6A":"117","A7A":"118","AXA":"119",\
"A01":"120","AA1":"121","A11":"122","A21":"123","A31":"124","A41":"125","A51":"126","A61":"127","A71":"128","AX1":"129",\
"A02":"130","AA2":"131","A12":"132","A22":"133","A32":"134","A42":"135","A52":"136","A62":"137","A72":"138","AX2":"139",\
"A03":"140","AA3":"141","A13":"142","A23":"143","A33":"144","A43":"145","A53":"146","A63":"147","A73":"148","AX3":"149",\
"A04":"150","AA4":"151","A14":"152","A24":"153","A34":"154","A44":"155","A54":"156","A64":"157","A74":"158","AX4":"159",\
"A05":"160","AA5":"161","A15":"162","A25":"163","A35":"164","A45":"165","A55":"166","A65":"167","A75":"168","AX5":"169",\
"A06":"170","AA6":"171","A16":"172","A26":"173","A36":"174","A46":"175","A56":"176","A66":"177","A76":"178","AX6":"179",\
"A07":"180","AA7":"181","A17":"182","A27":"183","A37":"184","A47":"185","A57":"186","A67":"187","A77":"188","AX7":"189",\
"A0X":"190","AAX":"191","A1X":"192","A2X":"193","A3X":"194","A4X":"195","A5X":"196","A6X":"197","A7X":"198","AXX":"199",\
"100":"200","1A0":"201","110":"202","120":"203","130":"204","140":"205","150":"206","160":"207","170":"208","1X0":"209",\
"10A":"210","1AA":"211","11A":"212","12A":"213","13A":"214","14A":"215","15A":"216","16A":"217","17A":"218","1XA":"219",\
"101":"220","1A1":"221","111":"222","121":"223","131":"224","141":"225","151":"226","161":"227","171":"228","1X1":"229",\
"102":"230","1A2":"231","112":"232","122":"233","132":"234","142":"235","152":"236","162":"237","172":"238","1X2":"239",\
"103":"240","1A3":"241","113":"242","123":"243","133":"244","143":"245","153":"246","163":"247","173":"248","1X3":"249",\
"104":"250","1A4":"251","114":"252","124":"253","134":"254","144":"255","154":"256","164":"257","174":"258","1X4":"259",\
"105":"260","1A5":"261","115":"262","125":"263","135":"264","145":"265","155":"266","165":"267","175":"268","1X5":"269",\
"106":"270","1A6":"271","116":"272","126":"273","136":"274","146":"275","156":"276","166":"277","176":"278","1X6":"279",\
"107":"280","1A7":"281","117":"282","127":"283","137":"284","147":"285","157":"286","167":"287","177":"288","1X7":"289",\
"10X":"290","1AX":"291","11X":"292","12X":"293","13X":"294","14X":"295","15X":"296","16X":"297","17X":"298","1XX":"299",\
"200":"300","2A0":"301","210":"302","220":"303","230":"304","240":"305","250":"306","260":"307","270":"308","2X0":"309",\
"20A":"310","2AA":"311","21A":"312","22A":"313","23A":"314","24A":"315","25A":"316","26A":"317","27A":"318","2XA":"319",\
"201":"320","2A1":"321","211":"322","221":"323","231":"324","241":"325","251":"326","261":"327","271":"328","2X1":"329",\
"202":"330","2A2":"331","212":"332","222":"333","232":"334","242":"335","252":"336","262":"337","272":"338","2X2":"339",\
"203":"340","2A3":"341","213":"342","223":"343","233":"344","243":"345","253":"346","263":"347","273":"348","2X3":"349",\
"204":"350","2A4":"351","214":"352","224":"353","234":"354","244":"355","254":"356","264":"357","274":"358","2X4":"359",\
"205":"360","2A5":"361","215":"362","225":"363","235":"364","245":"365","255":"366","265":"367","275":"368","2X5":"369",\
"206":"370","2A6":"371","216":"372","226":"373","236":"374","246":"375","256":"376","266":"377","276":"378","2X6":"379",\
"207":"380","2A7":"381","217":"382","227":"383","237":"384","247":"385","257":"386","267":"387","277":"388","2X7":"389",\
"20X":"390","2AX":"391","21X":"392","22X":"393","23X":"394","24X":"395","25X":"396","26X":"397","27X":"398","2XX":"399",\
"300":"400","3A0":"401","310":"402","320":"403","330":"404","340":"405","350":"406","360":"407","370":"408","3X0":"409",\
"30A":"410","3AA":"411","31A":"412","32A":"413","33A":"414","34A":"415","35A":"416","36A":"417","37A":"418","3XA":"419",\
"301":"420","3A1":"421","311":"422","321":"423","331":"424","341":"425","351":"426","361":"427","371":"428","3X1":"429",\
"302":"430","3A2":"431","312":"432","322":"433","332":"434","342":"435","352":"436","362":"437","372":"438","3X2":"439",\
"303":"440","3A3":"441","313":"442","323":"443","333":"444","343":"445","353":"446","363":"447","373":"448","3X3":"449",\
"304":"450","3A4":"451","314":"452","324":"453","334":"454","344":"455","354":"456","364":"457","374":"458","3X4":"459",\
"305":"460","3A5":"461","315":"462","325":"463","335":"464","345":"465","355":"466","365":"467","375":"468","3X5":"469",\
"306":"470","3A6":"471","316":"472","326":"473","336":"474","346":"475","356":"476","366":"477","376":"478","3X6":"479",\
"307":"480","3A7":"481","317":"482","327":"483","337":"484","347":"485","357":"486","367":"487","377":"488","3X7":"489",\
"30X":"490","3AX":"491","31X":"492","32X":"493","33X":"494","34X":"495","35X":"496","36X":"497","37X":"498","3XX":"499",\
"400":"500","4A0":"501","410":"502","420":"503","430":"504","440":"505","450":"506","460":"507","470":"508","4X0":"509",\
"40A":"510","4AA":"511","41A":"512","42A":"513","43A":"514","44A":"515","45A":"516","46A":"517","47A":"518","4XA":"519",\
"401":"520","4A1":"521","411":"522","421":"523","431":"524","441":"525","451":"526","461":"527","471":"528","4X1":"529",\
"402":"530","4A2":"531","412":"532","422":"533","432":"534","442":"535","452":"536","462":"537","472":"538","4X2":"539",\
"403":"540","4A3":"541","413":"542","423":"543","433":"544","443":"545","453":"546","463":"547","473":"548","4X3":"549",\
"404":"550","4A4":"551","414":"552","424":"553","434":"554","444":"555","454":"556","464":"557","474":"558","4X4":"559",\
"405":"560","4A5":"561","415":"562","425":"563","435":"564","445":"565","455":"566","465":"567","475":"568","4X5":"569",\
"406":"570","4A6":"571","416":"572","426":"573","436":"574","446":"575","456":"576","466":"577","476":"578","4X6":"579",\
"407":"580","4A7":"581","417":"582","427":"583","437":"584","447":"585","457":"586","467":"587","477":"588","4X7":"589",\
"40X":"590","4AX":"591","41X":"592","42X":"593","43X":"594","44X":"595","45X":"596","46X":"597","47X":"598","4XX":"599",\
"500":"600","5A0":"601","510":"602","520":"603","530":"604","540":"605","550":"606","560":"607","570":"608","5X0":"609",\
"50A":"610","5AA":"611","51A":"612","52A":"613","53A":"614","54A":"615","55A":"616","56A":"617","57A":"618","5XA":"619",\
"501":"620","5A1":"621","511":"622","521":"623","531":"624","541":"625","551":"626","561":"627","571":"628","5X1":"629",\
"502":"630","5A2":"631","512":"632","522":"633","532":"634","542":"635","552":"636","562":"637","572":"638","5X2":"639",\
"503":"640","5A3":"641","513":"642","523":"643","533":"644","543":"645","553":"646","563":"647","573":"648","5X3":"649",\
"504":"650","5A4":"651","514":"652","524":"653","534":"654","544":"655","554":"656","564":"657","574":"658","5X4":"659",\
"505":"660","5A5":"661","515":"662","525":"663","535":"664","545":"665","555":"666","565":"667","575":"668","5X5":"669",\
"506":"670","5A6":"671","516":"672","526":"673","536":"674","546":"675","556":"676","566":"677","576":"678","5X6":"679",\
"507":"680","5A7":"681","517":"682","527":"683","537":"684","547":"685","557":"686","567":"687","577":"688","5X7":"689",\
"50X":"690","5AX":"691","51X":"692","52X":"693","53X":"694","54X":"695","55X":"696","56X":"697","57X":"698","5XX":"699",\
"600":"700","6A0":"701","610":"702","620":"703","630":"704","640":"705","650":"706","660":"707","670":"708","6X0":"709",\
"60A":"710","6AA":"711","61A":"712","62A":"713","63A":"714","64A":"715","65A":"716","66A":"717","67A":"718","6XA":"719",\
"601":"720","6A1":"721","611":"722","621":"723","631":"724","641":"725","651":"726","661":"727","671":"728","6X1":"729",\
"602":"730","6A2":"731","612":"732","622":"733","632":"734","642":"735","652":"736","662":"737","672":"738","6X2":"739",\
"603":"740","6A3":"741","613":"742","623":"743","633":"744","643":"745","653":"746","663":"747","673":"748","6X3":"749",\
"604":"750","6A4":"751","614":"752","624":"753","634":"754","644":"755","654":"756","664":"757","674":"758","6X4":"759",\
"605":"760","6A5":"761","615":"762","625":"763","635":"764","645":"765","655":"766","665":"767","675":"768","6X5":"769",\
"606":"770","6A6":"771","616":"772","626":"773","636":"774","646":"775","656":"776","666":"777","676":"778","6X6":"779",\
"607":"780","6A7":"781","617":"782","627":"783","637":"784","647":"785","657":"786","667":"787","677":"788","6X7":"789",\
"60X":"790","6AX":"791","61X":"792","62X":"793","63X":"794","64X":"795","65X":"796","66X":"797","67X":"798","6XX":"799",\
"700":"800","7A0":"801","710":"802","720":"803","730":"804","740":"805","750":"806","760":"807","770":"808","7X0":"809",\
"70A":"810","7AA":"811","71A":"812","72A":"813","73A":"814","74A":"815","75A":"816","76A":"817","77A":"818","7XA":"819",\
"701":"820","7A1":"821","711":"822","721":"823","731":"824","741":"825","751":"826","761":"827","771":"828","7X1":"829",\
"702":"830","7A2":"831","712":"832","722":"833","732":"834","742":"835","752":"836","762":"837","772":"838","7X2":"839",\
"703":"840","7A3":"841","713":"842","723":"843","733":"844","743":"845","753":"846","763":"847","773":"848","7X3":"849",\
"704":"850","7A4":"851","714":"852","724":"853","734":"854","744":"855","754":"856","764":"857","774":"858","7X4":"859",\
"705":"860","7A5":"861","715":"862","725":"863","735":"864","745":"865","755":"866","765":"867","775":"868","7X5":"869",\
"706":"870","7A6":"871","716":"872","726":"873","736":"874","746":"875","756":"876","766":"877","776":"878","7X6":"879",\
"707":"880","7A7":"881","717":"882","727":"883","737":"884","747":"885","757":"886","767":"887","777":"888","7X7":"889",\
"70X":"890","7AX":"891","71X":"892","72X":"893","73X":"894","74X":"895","75X":"896","76X":"897","77X":"898","7XX":"899",\
"X00":"900","XA0":"901","X10":"902","X20":"903","X30":"904","X40":"905","X50":"906","X60":"907","X70":"908","XX0":"909",\
"X0A":"910","XAA":"911","X1A":"912","X2A":"913","X3A":"914","X4A":"915","X5A":"916","X6A":"917","X7A":"918","XXA":"919",\
"X01":"920","XA1":"921","X11":"922","X21":"923","X31":"924","X41":"925","X51":"926","X61":"927","X71":"928","XX1":"929",\
"X02":"930","XA2":"931","X12":"932","X22":"933","X32":"934","X42":"935","X52":"936","X62":"937","X72":"938","XX2":"939",\
"X03":"940","XA3":"941","X13":"942","X23":"943","X33":"944","X43":"945","X53":"946","X63":"947","X73":"948","XX3":"949",\
"X04":"950","XA4":"951","X14":"952","X24":"953","X34":"954","X44":"955","X54":"956","X64":"957","X74":"958","XX4":"959",\
"X05":"960","XA5":"961","X15":"962","X25":"963","X35":"964","X45":"965","X55":"966","X65":"967","X75":"968","XX5":"969",\
"X06":"970","XA6":"971","X16":"972","X26":"973","X36":"974","X46":"975","X56":"976","X66":"977","X76":"978","XX6":"979",\
"X07":"980","XA7":"981","X17":"982","X27":"983","X37":"984","X47":"985","X57":"986","X67":"987","X77":"988","XX7":"989",\
"X0X":"990","XAX":"991","X1X":"992","X2X":"993","X3X":"994","X4X":"995","X5X":"996","X6X":"997","X7X":"998","XXX":"999"}

tile = color_dict.get("X1X")
print(tile)