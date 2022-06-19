from typing import List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_schema, is_complainer, is_admin, is_approver
from managers.complaint import ComplaintManager
from shemas.request.complaint import ComplaintIn
from shemas.response.complaint import ComplaintOut

router = APIRouter(tags=["Complaints"])


@router.get("/complaints",
            dependencies=[Depends(oauth2_schema)],
            response_model=List[ComplaintOut])
async def get_all(request: Request):
    user = request.state.user
    return await ComplaintManager.get_complaints(user)


@router.post("/complaints",
             dependencies=[Depends(oauth2_schema), Depends(is_complainer)],
             response_model=ComplaintOut)
async def create(request: Request, complaint: ComplaintIn):
    user = request.state.user
    return await ComplaintManager.create(complaint.dict(), user)


@router.delete("/complaints/{complaint_id}",
               dependencies=[Depends(oauth2_schema), Depends(is_admin)],
               status_code=204)
async def delete(complaint_id: int):
    await ComplaintManager.delete(complaint_id)


@router.put("/complaints/{complaint_id}/approve",
            dependencies=[Depends(oauth2_schema), Depends(is_approver)],
            status_code=204)
async def approve(complaint_id: int):
    await ComplaintManager.approve(complaint_id)


@router.put("/complaints/{complaint_id}/reject",
            dependencies=[Depends(oauth2_schema), Depends(is_approver)],
            status_code=204)
async def reject(complaint_id: int):
    await ComplaintManager.reject(complaint_id)
