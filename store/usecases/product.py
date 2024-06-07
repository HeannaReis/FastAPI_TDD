'''
/store/usecase/product.py
'''
from typing import List
from uuid import UUID
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from store.db.postgres import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.core.exceptions import NotFoundException

class ProductUsecase:
    def __init__(self) -> None:
        self.db_client = db_client
        self.Base = self.db_client.get_base()

    async def create(self, body: ProductIn) -> ProductOut:
        async with self._get_session() as session:
            product_model = ProductModel(**body.model_dump())
            session.add(product_model)
            await session.commit()
            await session.refresh(product_model)
            return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        async with self._get_session() as session:
            result = await session.execute(select(ProductModel).where(ProductModel.id == id))
            product_model = result.scalars().first()
            if not product_model:
                raise NotFoundException(message=f"Product not found with filter: {id}")
            return ProductOut(**product_model.model_dump())

    async def query(self) -> List[ProductOut]:
        async with self._get_session() as session:
            result = await session.execute(select(ProductModel))
            return [ProductOut(**product.model_dump()) async for product in result]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        async with self._get_session() as session:
            result = await session.execute(select(ProductModel).where(ProductModel.id == id))
            product_model = result.scalars().first()
            if not product_model:
                raise NotFoundException(message=f"Product not found with filter: {id}")
            for field, value in body.model_dump(exclude_unset=True).items():
                setattr(product_model, field, value)
            await session.commit()
            return ProductUpdateOut(**product_model.model_dump())

    async def delete(self, id: UUID) -> bool:
        async with self._get_session() as session:
            result = await session.execute(select(ProductModel).where(ProductModel.id == id))
            product_model = result.scalars().first()
            if not product_model:
                raise NotFoundException(message=f"Product not found with filter: {id}")
            session.delete(product_model)
            await session.commit()
            return True

    async def _get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.db_client.get_session() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

product_usecase = ProductUsecase()