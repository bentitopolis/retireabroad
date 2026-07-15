import re

with open("th-deal-store.html", "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    (r'Reach Expats Now', r'เข้าถึงลูกค้าต่างชาติเลย'),
    (r'Drive real expat foot traffic\s*<span class="text-brand-green">directly</span><br\s*/>\s*to your door.', r'ดึงดูดลูกค้าชาวต่างชาติ <span class="text-brand-green">ให้มาที่ร้านของคุณ</span><br /> โดยตรง'),
    (r'Join the ReThaiRe Deal Store, offer a minimum 5% in-store discount, and instantly attract Thailand’s\s*community of high-value expats. It’s pure performance marketing—your only\s*investment is the discount given at the exact moment of sale.', r'เข้าร่วม ReThaiRe Deal Store มอบส่วนลดหน้าร้านขั้นต่ำ 5% และดึงดูดชุมชนชาวต่างชาติที่มีกำลังซื้อสูงในประเทศไทย การตลาดที่เน้นผลลัพธ์—คุณจะให้ส่วนลดก็ต่อเมื่อเกิดการซื้อขายจริงหน้าร้านเท่านั้น'),
    (r'Register on LINE', r'ลงทะเบียนผ่าน LINE'),
    (r'>\s*How it Works\s*<', r'>วิธีการทำงาน<'),
    (r'Why become a Deal Store partner\?', r'ทำไมถึงควรเป็นพาร์ทเนอร์กับ Deal Store?'),
    (r'Scan, Validate, and Sell', r'สแกน ตรวจสอบ และเพิ่มยอดขาย'),
    (r'Our dynamic QR code technology ensures complete control. When a ReThaiRe member wants to use their discount,\s*they show a unique QR code on their phone. You simply scan it with your camera in seconds to ensure it\'s\s*valid and close the sale securely.', r'เทคโนโลยีคิวอาร์โค้ดแบบไดนามิกของเราช่วยให้คุณควบคุมได้ทั้งหมด เมื่อสมาชิก ReThaiRe ต้องการใช้ส่วนลด พวกเขาจะแสดงคิวอาร์โค้ดบนมือถือ คุณเพียงแค่สแกนเพื่อตรวจสอบสิทธิ์ในไม่กี่วินาที และปิดการขายได้อย่างปลอดภัย'),
    (r'Guaranteed In-Store Sales', r'รับประกันยอดขายหน้าร้านจริง'),
    (r'We bridge the gap between online discovery and physical foot traffic. With the Deal Store, your marketing\s*investment is purely performance-based. You only grant the discount when the customer is standing at your\s*checkout, ready to pay.', r'เราเชื่อมโยงการค้นหาออนไลน์กับการเดินทางมาที่ร้านจริงๆ การลงทุนทางการตลาดของคุณจะขึ้นอยู่กับผลลัพธ์เท่านั้น คุณจะให้ส่วนลดเมื่อลูกค้ามายืนอยู่หน้าเคาน์เตอร์และพร้อมจ่ายเงินแล้วเท่านั้น'),
    (r'The FIRE & Expat Audience', r'กลุ่มลูกค้าชาวต่างชาติที่มีกำลังซื้อสูง'),
    (r'Our users aren\'t tourists. They are long-term expats, remote workers, and FIRE \(Financial\s*Independence, Retire Early\) community members building a life in Thailand. They are loyal, high-spending,\s*and value smart\s*local partnerships.', r'ผู้ใช้ของเราไม่ใช่นักท่องเที่ยวทั่วไป แต่เป็นชาวต่างชาติที่พำนักระยะยาว คนทำงานทางไกล และกลุ่ม FIRE ที่กำลังสร้างชีวิตในประเทศไทย พวกเขามีความภักดีต่อแบรนด์ มีกำลังซื้อสูง และมองหาพาร์ทเนอร์ท้องถิ่นที่เชื่อถือได้'),
    (r'Setup in Minutes via LINE', r'ตั้งค่าผ่าน LINE ในไม่กี่นาที'),
    (r'Add our LINE Official Account, submit your business details, and set a minimum 5% discount. You are\s*instantly listed in the ReThaiRe app directory.', r'เพิ่มเพื่อนผ่าน LINE Official Account ของเรา ส่งข้อมูลธุรกิจ และตั้งค่าส่วนลดขั้นต่ำ 5% ร้านของคุณจะไปอยู่บนแอปพลิเคชัน ReThaiRe ทันที'),
    (r'Welcome ReThaiRe Members', r'ต้อนรับสมาชิก ReThaiRe'),
    (r'Expats discover your offer in the app and visit your physical store. At the checkout, they will present\s*a unique QR code on their phone screen.', r'ชาวต่างชาติจะเห็นข้อเสนอของคุณในแอปและเดินทางมาที่ร้าน เมื่อถึงเวลาชำระเงิน พวกเขาจะแสดงคิวอาร์โค้ดบนหน้าจอมือถือ'),
    (r'Scan to Validate', r'สแกนเพื่อรับสิทธิ์'),
    (r'Use any smartphone camera to scan the customer\'s screen. The code is verified instantly, you apply the\s*discount, and secure a new customer.', r'ใช้กล้องสมาร์ทโฟนทั่วไปสแกนหน้าจอลูกค้า ระบบจะตรวจสอบโค้ดทันที คุณมอบส่วนลด และได้ลูกค้าประจำคนใหม่'),
    (r'Is your business a match for our Expat community\?', r'ธุรกิจของคุณเหมาะกับชุมชนชาวต่างชาติของเราหรือไม่?'),
    (r'The ReThaiRe Deal Store is designed for everyday lifestyle, health, and local experiences. To maintain quality, all partners go through a quick approval process.', r'ReThaiRe Deal Store ออกแบบมาเพื่อไลฟ์สไตล์ สุขภาพ และประสบการณ์ท้องถิ่นในชีวิตประจำวัน เพื่อรักษาคุณภาพ พาร์ทเนอร์ทั้งหมดจะผ่านขั้นตอนการอนุมัติอย่างรวดเร็ว'),
    (r'We are looking for:', r'เรากำลังมองหา:'),
    (r'Restaurants, Cafes & Bars', r'ร้านอาหาร คาเฟ่ และบาร์'),
    (r'Clinics, Dentists & Wellness', r'คลินิก ทันตกรรม และสุขภาพ'),
    (r'Spas, Salons & Gyms', r'สปา ซาลอน และฟิตเนส'),
    (r'Retail Stores & Everyday Services', r'ร้านค้าปลีกและบริการทั่วไป'),
    (r'Tours & Local Experiences', r'ทัวร์และประสบการณ์ท้องถิ่น'),
    (r'Health Insurance, Visas', r'ประกันสุขภาพ อสังหาริมทรัพย์ และวีซ่า'), # Wait, original HTML had Health Insurance, Visas. User map says "Health Insurance, Real Estate & Visas".
    (r'Not a fit:', r'ธุรกิจที่ไม่เข้าร่วม:'),
    (r'Real Estate & Land Sales', r'การขายที่ดิน'),
    (r'High-Risk Investments', r'การลงทุนที่มีความเสี่ยงสูง'),
    (r'B2B Industrial Services', r'บริการอุตสาหกรรมแบบ B2B'),
    (r'Unverified/Unlicensed Businesses', r'ธุรกิจที่ไม่ได้รับการยืนยัน/ไม่มีใบอนุญาต'),
    (r'Ready to become an approved Deal Store partner\?', r'พร้อมที่จะเป็นพาร์ทเนอร์ที่ได้รับการอนุมัติจาก Deal Store แล้วหรือยัง?'),
    (r'Apply now via LINE', r'สมัครเลยผ่าน LINE')
]

for pattern, replacement in replacements:
    # Use re.sub with regex to replace any spacing variations
    text, num_subs = re.subn(pattern, replacement, text, flags=re.MULTILINE)
    if num_subs == 0:
        print(f"Warning: pattern '{pattern}' not found!")

with open("th-deal-store.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
