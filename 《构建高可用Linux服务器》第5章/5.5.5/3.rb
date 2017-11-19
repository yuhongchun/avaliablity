newrecord("bid-east.example.net") do |query, answer|
    ips = ["54.175.1.2", "54.164.1.2", "52.6.1.2","54.164.1.2", "54.175.1.2","54.175.1.3","54.175.1.4","52.4.1.2"…… ]
    #bidder机器大约20台左右，公网IP作了无害处理
    ips = ips.randomize([1, 1, 1, 1, 1, 1, 1, 1])
    answer.shuffle false
    answer.ttl 30
    answer.content ips[0]
    answer.content ips[1]
    answer.content ips[2]
    answer.content ips[3]
    answer.content ips[4]
    answer.content ips[5]
    answer.content ips[6]
    answer.content ips[7]
end
