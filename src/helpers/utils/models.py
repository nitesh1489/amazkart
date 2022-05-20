from dataclasses import dataclass, field,asdict

@dataclass(order=True)
class Product:
    product:str=field(compare=False,repr=True)
    price:str=field(compare=False,repr=True)
    specifications:str=field(compare=False)
    thumbnail:str=field(compare=False,repr=False)
    discounted_price:str=field(compare=False,repr=False)
    rating:str=field(compare=False,repr=False)
    product_url:str=field(compare=False,repr=False)
    
    def to_dict(self):
        return asdict(self)