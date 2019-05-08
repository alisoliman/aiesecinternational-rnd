SELECT p.id,
    to_char(min(opportunity_applications.created_at)
:: DATE,
               'YYYY-MM-DD HH24:MI:SS'),
       to_char
(p.created_at :: DATE,
               'YYYY-MM-DD HH24:MI:SS')
from opportunity_applications
         FULL OUTER JOIN people p on opportunity_applications.person_id = p.id
WHERE p.id = %d
group by p.id
order by p.created_at;