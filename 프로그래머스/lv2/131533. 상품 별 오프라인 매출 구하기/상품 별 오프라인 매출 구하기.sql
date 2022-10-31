select p.product_code,  p.price * sum(off.sales_amount) as SALES
from product p 
join OFFLINE_SALE  off on p.product_id = off.product_id
group by p.product_code
order by sales desc, p.product_code