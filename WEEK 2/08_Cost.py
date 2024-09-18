"""
Program which calculate the Shipping Cost
Author = Vraj Prajapati
"""

cover_prize_book=25.00
total_copies=70
first_copy_shippingcost=2.5
other_copy_shippingcost =0.75
discount= cover_prize_book*0.40
cost_of_firstbook= first_copy_shippingcost+(cover_prize_book-discount)
cost_of_otherbooks=(other_copy_shippingcost*59)+(14.97*59)
wholesale= cost_of_firstbook + cost_of_otherbooks
print("discount:=",discount)
print("cost of firstbook:=",cost_of_firstbook)
print("cost of othertbooks:=",cost_of_otherbooks)
print("total wholesale cost:=",wholesale,sep="")
