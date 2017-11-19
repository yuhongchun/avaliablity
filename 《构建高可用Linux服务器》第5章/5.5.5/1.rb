module Pdns
  newrecord("www.your.net") do |query, answer|
    case country(query[:remoteip])
      when "US", "CA"
        answer.content "64.xx.xx.245"

      when "ZA", "ZW"
        answer.content "196.xx.xx.10"

      else
        answer.content "78.xx.xx.140"
      end
  end
end
