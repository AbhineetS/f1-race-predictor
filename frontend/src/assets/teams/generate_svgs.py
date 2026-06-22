import os

svgs = {
    "ferrari.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="#DC0000"/><text x="50" y="65" font-family="sans-serif" font-size="60" font-weight="bold" fill="#FFF" text-anchor="middle">F</text></svg>',
    "mercedes.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="45" fill="none" stroke="#00D2BE" stroke-width="8"/><path d="M50 5 L50 50 M15 75 L50 50 M85 75 L50 50" stroke="#00D2BE" stroke-width="8"/></svg>',
    "mclaren.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><path d="M10 80 Q 50 20 90 80" fill="none" stroke="#FF8700" stroke-width="20" stroke-linecap="round"/></svg>',
    "red_bull.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="#FFD700"/><path d="M10 50 L40 50 L40 30 Z" fill="#DC0000"/><path d="M90 50 L60 50 L60 30 Z" fill="#DC0000"/></svg>',
    "aston_martin.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="40" y="30" fill="#006F62"/><text x="50" y="58" font-family="sans-serif" font-size="24" font-weight="bold" fill="#FFF" text-anchor="middle">ASTON</text></svg>',
    "williams.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><text x="50" y="70" font-family="sans-serif" font-size="70" font-weight="bold" fill="#005AFF" text-anchor="middle">W</text></svg>',
    "alpine.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><path d="M50 20 L20 80 L80 80 Z" fill="#0090FF"/><text x="50" y="70" font-family="sans-serif" font-size="40" font-weight="bold" fill="#FFF" text-anchor="middle">A</text></svg>',
    "haas.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="45" fill="#B6BABD"/><text x="50" y="65" font-family="sans-serif" font-size="45" font-weight="bold" fill="#05070D" text-anchor="middle">H</text></svg>',
    "sauber.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" rx="20" fill="#52E252"/><text x="50" y="65" font-family="sans-serif" font-size="45" font-weight="bold" fill="#000" text-anchor="middle">S</text></svg>',
    "racing_bulls.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="#6692FF"/><text x="50" y="65" font-family="sans-serif" font-size="40" font-weight="bold" fill="#FFF" text-anchor="middle">RB</text></svg>',
    "audi.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="25" cy="50" r="15" fill="none" stroke="#FFF" stroke-width="5"/><circle cx="45" cy="50" r="15" fill="none" stroke="#FFF" stroke-width="5"/><circle cx="65" cy="50" r="15" fill="none" stroke="#FFF" stroke-width="5"/><circle cx="85" cy="50" r="15" fill="none" stroke="#FFF" stroke-width="5"/></svg>',
    "cadillac.svg": '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="30" width="60" height="40" fill="#FFD700" stroke="#FFF" stroke-width="4"/><rect x="25" y="35" width="20" height="30" fill="#DC0000"/><rect x="55" y="35" width="20" height="30" fill="#000"/></svg>',
}

for name, content in svgs.items():
    with open(name, "w") as f:
        f.write(content)
