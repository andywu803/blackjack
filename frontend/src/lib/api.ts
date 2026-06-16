const BASE = 'http://localhost:8000'

export async function apiNewGame() {
    const res = await fetch(`${BASE}/game/new`, { method: 'POST'});
    return res.json();
}

export async function apiHit() {
    const res = await fetch(`${BASE}/game/hit`, { method: 'POST'});
    return res.json();
}

export async function apiStand() {
    const res = await fetch(`${BASE}/game/hit`, { method: 'POST'});
    return res.json();
}