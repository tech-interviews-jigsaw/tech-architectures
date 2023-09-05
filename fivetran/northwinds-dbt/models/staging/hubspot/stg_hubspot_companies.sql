WITH source as (
  SELECT * FROM {{ source('hubspot', 'contacts')}} 
), 
renamed as (
    SELECT 
    concat('hubspot-',replace(lower(business_name), ' ', '-')) as company_id,
    business_name as name
    FROM source
    GROUP BY name
    )
SELECT * FROM renamed