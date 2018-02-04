
import http.client, urllib.request, urllib.parse, urllib.error, base64, json, requests
from pprint import pprint

INPUT_TEXT = "Who. You're listening to the are going to City pod cast I'm John Gaunt and recently we were in the arts district of Los Angeles for. A five day extravaganza of all things to do with next generation mobility and while we were there we spoke with Stella leak who is the president of the motors North America. Thank you very much for joining us today yes thank you right can you give us sort of like the broad overview of B.Y.T. Motors who are you serving as customers and sort of the main problems that you're solving OK so. Idea. Of targeting area been why is it about his story and also for those dollar a second Pods the buses chucks and is that you. And also like a skier. Then you can see B.Y.D. is not the only target for one area up in S. But it would target the whole time to the CIM isn't named stand a full names James that we can Jerry latches to directly fund by the sunshine then we can use a better way to store the they'll like a use this clean energy to power to put Haitian e-mail some day. Be operated by the factory and is the kind of the whole eco system from the solar power collection all the way to the distribution to the bus to the bus then also you can view us here buses no longer need a public transportation you can you prove that using experience to be cleaner and less noise then the people were sitting inside the bus more like a comfortable and there's any joy and there was also Today's a life I eat technology you. Go it was wife by you can also use your phone to see the boss when well arriving asked who made the plane your schedule to distaste So obviously it was a you you touch into the you have to fake Asian you make it a stock to you know Asian here Iran does this you better vacation with like a jobless car then the first application as a bleed will be either a bus application and a placating into that area it's easier and also make more sense right then this will build a foundation to fall future travel is car let's work backwards from sort of the electric bus eventually to the power generation Yes So with the electric bus where you working in the US we working with the fifty different a transit Ajax and also private customer you can imagine all first cus my US is a Stanford University then we also now working with the U.C. system so that you see over in U.C. San Francisco U.C.L.A. and also as a school and Apple it as a private to oppose Facebook is running buses plus we'll have the public transit agent OK we'll have a now we grow every week when adding that new customer like it we just received a largest order from a much oil was a sixty and a plus five as an option then via I think is this a small baby a staff pull their twenty's thirty's one hundred percent failure mission at like it buses go OK So these are one hundred percent electric buses and they are the same size as we are accustomed to how many passengers can like cure that if you're talking about the alien much gold they have the different buses and all the way from such a five food to forty four to food and also to sixty sixty food I take a bus small medium and large small began to lie to them we have private. House mighty Bay Area welcome with them for. Us we will have a press release by Maybe next year first quarter next year but I'll customize had peg that they all took big culprit very important. Like a chance eighteen's. They out and. For Chauncey eating the US to announce one hundred percent yesterday cation they made this announcement last year beginning of last year but the then back end of next year as you will want their wakes cute the entire fleet as day entire fleet to. Bust so then their bus fleet also is a forty foot and a transit bus and they're also forty five foot coach bus and I take up bus then they're going to offload the service not only region but also for the lawn driving distance from Lancaster all the way to Los Angeles and his end of his stop here go back so that's kind of. What gave you idea like a full monty almost a cover all the condition the public transit needs OK And these these electric buses and let's let's use a large size and what is the range I mean all how far can they go on a single battery charge that's so weak we gave it the SPAG always account so to just say like a one hundred eighty mouse OK then the C.E.O. He's joking with us a few ideas big Elia what we say why because I was saying I gave one hundred fifty miles but I tried this because we can go to two hundred mice so then this kind of buzz we can go to two hundred fifty miles so get are you surprised yes I don't. Know they all say that this allies like it because they like it we always surprise them with performance. One hundred eighty miles going T. Buy the no money did customer Y. Use maybe got the two hundred mile to two hundred fifty miles and also this is I keep a bus you can carry and I came. One hundred ten passengers. Says And you can also do to our choice is means like you feel has some very good doing to supplement to chide this bus. Wait almost surveys full five kilometers per day wow yeah OK well if that is that as a bus Let's move up "
KEVIN_TEXT = "You're listening to the Ogma city podcast I'm John Gaunt and we're in Los Angeles at the L.A. come ocean which is a five day extravaganza of everything to do with next generation mobility from technology to policy and everything in between and I'm joined by Kevin North who is the co-founder and C.E.O. of AMP air which is a very unique company in the aviation space so Kevin thanks for coming thanks for having me OK can you start by giving sort of the sixty second overview of AMP air and basically what you're trying to do sure yeah so we we found a vampire on this question of what is the highest performance aircraft uniquely enabled by electric vehicle technology that we've got that desire to create something that's always been perceived as impossible and to make that a reality so pairing the great technology that we see in the electrification of ground transportation we're now taking that technology to the air while we're focused on is an entry point into the market with conventional aircraft Well we believe in a future of you know high speed jets and vertical takeoff and landing jets as well fully electric for those really the first step is more conventional aircraft so replacing what have been turbo prop aircraft initially and that's where we're focused today we're based here in the heart of Los Angeles in the L.A. clean tech incubator we've got a full team of eight located here and we're making great progress on the market and technically So you are literally talking about a battery powered airplane that's correct yeah big battery of some one would hope. One would hope so you know let's let let's let let's talk about aside from the power sort of what is completely new about this design and then what are you piggybacking on previous state of State of the art right so there are many new opportunities when you're designing a new aircraft right the exciting future of electric aviation is where you do new integration techniques so that's how do you integrate your propulsion in order to get boundary layer ingestion another efficiency. As with the planes however the very first step for us is on sleep a little less exciting than that we're retrofitting existing planes so that's a very pragmatic first step utilizing existing technologies so the big unable or so for us energy density of the batteries but then you've got the power density of the motors and the efficiency of those motors as well plus all the connective tissue like the inverters and controllers and whatnot is the aircraft more or less the same weight as the piston engine or engine that you're replacing correct so the the aircraft itself will be the full total weight and what will be doing is replacing the fuel weight and those heavy engines motors are much less much less heavy we will be replacing those with the electric vehicle components in certain cases you may choose to put more batteries and decrease the payload capacity of that aircraft in order to maybe make a little bit of a further flight and when you're you know when you're putting these these designs together what lessons are you really pulling from the electric car industry and then where where's the boundary that we're just like That's nice but I am going we're going to air so there are a lot of best practices that were riding the coattails of the ground vehicle transition right the the electrification of ground vehicles has been amazing over the last few years really leveraging that as the enabler for electric aviation so that how do you how do you program your controllers a lot of the best practices from a technical aspect but there are corner cases where you can't optimize an airplane the same as you optimize a car imagine your thermal system on a car you need to be able to handle the heating of the system as you're accelerating off of stop signs and and stopping at the next sign with an aircraft you really don't have that type of a duty cycle you've got taxiing taking off and climbing and then cruising and so this means we can optimize that thermal system to be much lower weight and then more weight efficient for the specific use case we have so that's kind of where the line is drawn a lot of the underlying components are going to be very similar though well of which. Talking about the aircraft themselves how how big are we talking I mean like how many passengers can we take in one of these aircraft Yes So our target is a nine passenger turbo prop sized aircraft so that single single engine turboprop these these aircraft are commonly used by thin haul operators or operators that do puddle jumping so imagine hopping between islands in Hawaii or or other regional deliveries there are thousands of daily scheduled flights of this type of aircraft the it depends on the load factor for the particular airline on which will aim for the nine passenger be willing to maybe take it down to seven passengers or in some cases you might even need an one thousand passenger aircraft the little take is a bit longer to get that size right and then for the pilots of these aircraft what are the new skills they need to "

subscription_key="968ffd2f58d44651b08a8667963bebe6"
assert subscription_key

bing7_sub_key = 'a9b1b4da5cb84adcbccfee1161983206'

VOICEBASE_URL = 'https://app.voicebase.com/my_account/voice_file_detail/57845402'

VB_KEYWORDS_SELECTOR = "ul.vbs-topics-list"

    
key_phrase_api_url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases?%s"
video_search_url = "https://api.cognitive.microsoft.com/bing/v7.0/videos/search"
web_search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

documents = { 'documents': [
    { 'language': 'en','id':'string', 'text': KEVIN_TEXT }
]}


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '968ffd2f58d44651b08a8667963bebe6',
}

params = urllib.parse.urlencode({
        ## EMPTY FOR GOOD REASONS
})



headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
json_data = json.loads(response.text)
array_of_keywords = json_data["documents"][0]['keyPhrases']


print("Source Audio link = " + "https://soundcloud.com/user-413798199/ac-la-comotion-the-electric-future-of-air-travel-with-ampaires-kevin-noertker")

counter = 0
searches  = 3
while(counter < searches):
    search_term = array_of_keywords[counter]
    counter +=1
    headers = {"Ocp-Apim-Subscription-Key" : bing7_sub_key }
    params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
    video_response = requests.get(video_search_url, headers=headers, params=params)
    web_response = requests.get(web_search_url, headers=headers, params=params)
    video_response.raise_for_status()
    web_response.raise_for_status()
    video_search_results = video_response.json()
    web_search_results = web_response.json()


    videos = json.loads(video_response.text)
    links = json.loads(web_response.text)
    #debug_obj = links
    #pprint(debug_obj)
    video_result = videos["value"][0]["contentUrl"]
    web_result = links["webPages"]["value"][0]["url"]
    pprint(array_of_keywords[counter])
    print(video_result)
    print(web_result)


#for term in serarch_term


