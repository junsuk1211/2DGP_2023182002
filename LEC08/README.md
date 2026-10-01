# Drill #8 — Naruto Animation Viewer

## 구현 목표
- `run`, `walk`, `jump`, `Y combo` 네 가지 애니메이션
- 화면 중앙에서 크게 재생
- 각 동작을 5회 반복하고 1초 정지한 다음 다음 동작으로 전환
- 전체 순서를 무한 반복
- 서로 다른 프레임 크기와 프레임 수 지원

## 실행
```powershell
python -m pip install -r LEC08/requirements.txt
python LEC08/animation_viewer.py
```
`LEC08` 안에서 `python animation_viewer.py`로 실행해도 됩니다.
창 닫기 또는 ESC로 종료합니다. 자동으로 동작을 순환하므로 별도 입력은 필요 없습니다.

## 프레임 구성과 추가 점수 구현
| 동작 | 프레임 수 | 초당 프레임 | 5회 재생 시간 |
|---|---:|---:|---:|
| run | 6 | 12 | 2.5초 |
| walk | 6 | 10 | 3초 |
| jump | 5 | 8 | 3.125초 |
| Y combo | 12 | 12 | 5초 |

한 순환은 정지 시간 4초를 포함해 17.625초입니다.
가변 크기의 복잡한 원본 시트를 사용하며 프레임별 좌표·너비·높이를 JSON으로 저장합니다.
애니메이션마다 프레임 수가 달라도 각 동작의 실제 프레임 수로 5회 반복합니다.
따라서 **프레임 크기 차이 지원**, **애니메이션별 프레임 수 차이 지원**을 모두 구현했습니다.
1000×800 화면에서 픽셀을 8배 확대해 각 동작의 최대 캐릭터 높이를 약 400~600px로 표시합니다.
웅크리는 자세는 원본 자세를 유지하므로 해당 프레임의 높이는 줄어듭니다.
동작 전체 영역을 화면 중앙에 배치하고 발 위치를 고정합니다.

## 에셋 재생성
```powershell
python -m pip install -r LEC08/tools/requirements.txt
python LEC08/tools/extract_sprites.py
```
원본은 사용자가 제공한 Nintendo DS 게임의 Naruto 스프라이트 시트입니다.
시트에 적힌 출처: Naruto Shippuden: Ninja Council 4, ripped by Mr. C.
원본 크레딧을 포함한 시트를 `assets/naruto_source.png`에 보존했습니다.
초록 배경 `(0,128,0)`을 투명하게 처리하고 네 동작만 아틀라스로 추출합니다.

## 검증
```powershell
python -m unittest discover -s LEC08 -v
```
