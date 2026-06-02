console.log("JS LOADED")

// State
let characters = [];
let currentCharacterId = null;
let editMode = false;
let deleteCharacterId = null;

// DOM Elements
const charactersList = document.getElementById('charactersList');
const btnNewCharacter = document.getElementById('btnNewCharacter');
const btnMenu = document.getElementById('btnMenu');
const menuDropdown = document.getElementById('menuDropdown');
const btnLoadDummy = document.querySelector('#menuDropdown button');
const btnDiceRoll = document.getElementById('btnDiceRoll');
const searchBox = document.getElementById('searchBox');
const characterModal = document.getElementById('characterModal');
const detailsModal = document.getElementById('detailsModal');
const diceModal = document.getElementById('diceModal');
const deleteModal = document.getElementById('deleteModal');
const characterForm = document.getElementById('characterForm');
const modalTitle = document.getElementById('modalTitle');

// Form Elements
const charNameInput = document.getElementById('charName');
const charLevelInput = document.getElementById('charLevel');
const charRaceInput = document.getElementById('charRace');
const charClassInput = document.getElementById('charClass');
const statInputs = {
    str: document.getElementById('statStr'),
    dex: document.getElementById('statDex'),
    con: document.getElementById('statCon'),
    int: document.getElementById('statInt'),
    wis: document.getElementById('statWis'),
    cha: document.getElementById('statCha')
};
const modifiers = {
    str: document.getElementById('modStr'),
    dex: document.getElementById('modDex'),
    con: document.getElementById('modCon'),
    int: document.getElementById('modInt'),
    wis: document.getElementById('modWis'),
    cha: document.getElementById('modCha')
};
const btnRandomizeStats = document.getElementById('btnRandomizeStats');
const btnAddItem = document.getElementById('btnAddItem');
const newInventoryItem = document.getElementById('newInventoryItem');
const inventoryList = document.getElementById('inventoryList');
const btnCancel = document.getElementById('btnCancel');

// Utility Functions
function calculateModifier(stat) {
    return Math.floor((stat - 10) / 2);
}

function updateModifiers() {
    Object.keys(statInputs).forEach(stat => {
        const value = parseInt(statInputs[stat].value) || 10;
        const mod = calculateModifier(value);
        const sign = mod >= 0 ? '+' : '';
        modifiers[stat].textContent = `(${sign}${mod})`;
    });
}

function openModal(modal) {
    modal.classList.add('show');
}

function closeModal(modal) {
    modal.classList.remove('show');
}

function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error';
    errorDiv.textContent = message;
    document.getElementById('notificationsContainer').appendChild(errorDiv);
    setTimeout(() => {
        errorDiv.style.animation = 'slideOutUp 0.3s ease-out';
        setTimeout(() => errorDiv.remove(), 300);
    }, 5000);
}

function showSuccess(message) {
    const successDiv = document.createElement('div');
    successDiv.className = 'success';
    successDiv.textContent = message;
    document.getElementById('notificationsContainer').appendChild(successDiv);
    setTimeout(() => {
        successDiv.style.animation = 'slideOutUp 0.3s ease-out';
        setTimeout(() => successDiv.remove(), 300);
    }, 3000);
}

// API Functions
async function fetchCharacters() {
    try {
        const response = await fetch('/api/characters');
        characters = await response.json();
        renderCharacters(characters);
    } catch (error) {
        showError('Failed to load characters');
        console.error(error);
    }
}

async function createCharacter(data) {
    try {
        const response = await fetch('/api/characters', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to create character');
        }
        
        showSuccess('Character created successfully!');
        fetchCharacters();
    } catch (error) {
        showError(error.message);
    }
}

async function updateCharacter(id, data) {
    try {
        const response = await fetch(`/api/characters/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to update character');
        }
        
        showSuccess('Character updated successfully!');
        fetchCharacters();
    } catch (error) {
        showError(error.message);
    }
}

async function deleteCharacter(id) {
    deleteCharacterId = id;
    const char = characters.find(c => c.id === id);
    document.getElementById('deleteMessage').textContent = `Are you sure you want to delete "${char.name}"? This cannot be undone.`;
    openModal(deleteModal);
}

async function rollDice() {
    try {
        const response = await fetch('/api/roll-dice', { 
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error('Failed to roll dice');
        const data = await response.json();
        document.getElementById('diceResult').textContent = data.result;
        openModal(diceModal);
    } catch (error) {
        showError('Failed to roll dice: ' + error.message);
        console.error(error);
    }
}

async function randomizeStats() {
    try {
        const response = await fetch('/api/randomize-stats');
        const stats = await response.json();
        Object.keys(stats).forEach(stat => {
            statInputs[stat].value = stats[stat];
        });
        updateModifiers();
    } catch (error) {
        showError('Failed to randomize stats');
    }
}

// Rendering
function renderCharacters(charList) {
    charactersList.innerHTML = '';
    
    if (charList.length === 0) {
        charactersList.innerHTML = '<div class="loading">No characters yet. Create one to get started!</div>';
        return;
    }
    
    charList.forEach(char => {
        const card = document.createElement('div');
        card.className = 'character-card';
        
        const statsPreview = `
            <div class="stats-preview">
                <div class="stat-item"><span class="stat-label">💪</span><span class="stat-val">${char.stats.str}</span></div>
                <div class="stat-item"><span class="stat-label">🏃</span><span class="stat-val">${char.stats.dex}</span></div>
                <div class="stat-item"><span class="stat-label">❤️</span><span class="stat-val">${char.stats.con}</span></div>
                <div class="stat-item"><span class="stat-label">🧠</span><span class="stat-val">${char.stats.int}</span></div>
                <div class="stat-item"><span class="stat-label">👁️</span><span class="stat-val">${char.stats.wis}</span></div>
                <div class="stat-item"><span class="stat-label">✨</span><span class="stat-val">${char.stats.cha}</span></div>
            </div>
        `;
        
        card.innerHTML = `
            <h3>${char.name}</h3>
            <div class="meta">
                <span class="level">Lvl ${char.level}</span>
                <span>${char.race} ${char.class}</span>
            </div>
            ${statsPreview}
        `;
        card.addEventListener('click', () => showCharacterDetails(char));
        charactersList.appendChild(card);
    });
}

function showCharacterDetails(char) {
    currentCharacterId = char.id;
    const detailsDiv = document.getElementById('charDetails');
    
    let inventoryHtml = '';
    if (char.inventory && char.inventory.length > 0) {
        inventoryHtml = `
            <div class="inventory-display">
                <h4>Inventory</h4>
                <ul>
                    ${char.inventory.map(item => `<li>${item}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    detailsDiv.innerHTML = `
        <div class="character-details">
            <div class="detail-header">
                <h3>${char.name}</h3>
                <p style="color: #999;">${char.race} ${char.class} - Level ${char.level}</p>
            </div>
            
            <div class="detail-stats">
                <div class="stat-box">
                    <div class="stat-name">💪 Strength</div>
                    <div class="stat-value">${char.stats.str}</div>
                    <div class="stat-mod">${char.stats.str >= 10 ? '+' : ''}${Math.floor((char.stats.str - 10) / 2)}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-name">🏃 Dexterity</div>
                    <div class="stat-value">${char.stats.dex}</div>
                    <div class="stat-mod">${char.stats.dex >= 10 ? '+' : ''}${Math.floor((char.stats.dex - 10) / 2)}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-name">❤️ Constitution</div>
                    <div class="stat-value">${char.stats.con}</div>
                    <div class="stat-mod">${char.stats.con >= 10 ? '+' : ''}${Math.floor((char.stats.con - 10) / 2)}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-name">🧠 Intelligence</div>
                    <div class="stat-value">${char.stats.int}</div>
                    <div class="stat-mod">${char.stats.int >= 10 ? '+' : ''}${Math.floor((char.stats.int - 10) / 2)}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-name">👁️ Wisdom</div>
                    <div class="stat-value">${char.stats.wis}</div>
                    <div class="stat-mod">${char.stats.wis >= 10 ? '+' : ''}${Math.floor((char.stats.wis - 10) / 2)}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-name">✨ Charisma</div>
                    <div class="stat-value">${char.stats.cha}</div>
                    <div class="stat-mod">${char.stats.cha >= 10 ? '+' : ''}${Math.floor((char.stats.cha - 10) / 2)}</div>
                </div>
            </div>
            
            ${inventoryHtml}
        </div>
    `;
    
    openModal(detailsModal);
}

function resetForm() {
    characterForm.reset();
    charLevelInput.value = 1;
    Object.keys(statInputs).forEach(stat => statInputs[stat].value = 10);
    updateModifiers();
    inventoryList.innerHTML = '';
    editMode = false;
    currentCharacterId = null;
}

// Event Listeners
btnNewCharacter.addEventListener('click', () => {
    resetForm();
    modalTitle.textContent = 'Create New Character';
    editMode = false;
    openModal(characterModal);
});

// Dropdown menu toggle
btnMenu.addEventListener('click', (e) => {
    e.stopPropagation();
    menuDropdown.classList.toggle('show');
});

// Close dropdown when clicking elsewhere
document.addEventListener('click', (e) => {
    if (!e.target.closest('.menu-dropdown')) {
        menuDropdown.classList.remove('show');
    }
});

btnLoadDummy.addEventListener('click', async () => {
    menuDropdown.classList.remove('show');
    openModal(document.getElementById('loadDataWarningModal'));
});

document.getElementById('btnConfirmLoadData').addEventListener('click', async () => {
    try {
        const response = await fetch('/api/load-dummy', { method: 'POST' });
        if (!response.ok) throw new Error('Failed to load dummy data');
        showSuccess('Sample data loaded successfully!');
        fetchCharacters();
        closeModal(document.getElementById('loadDataWarningModal'));
    } catch (error) {
        showError(error.message);
    }
});

document.getElementById('btnCancelLoadData').addEventListener('click', () => {
    closeModal(document.getElementById('loadDataWarningModal'));
});

btnRandomizeStats.addEventListener('click', (e) => {
    e.preventDefault();
    randomizeStats();
});

btnAddItem.addEventListener('click', (e) => {
    e.preventDefault();
    const item = newInventoryItem.value.trim();
    if (!item) {
        showError('Please enter an item');
        return;
    }
    
    const tag = document.createElement('div');
    tag.className = 'inventory-tag';
    tag.innerHTML = `
        ${item}
        <span class="remove">×</span>
    `;
    tag.querySelector('.remove').addEventListener('click', () => tag.remove());
    inventoryList.appendChild(tag);
    newInventoryItem.value = '';
});

characterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const inventory = Array.from(inventoryList.querySelectorAll('.inventory-tag'))
        .map(tag => tag.textContent.replace('×', '').trim());
    
    const data = {
        name: charNameInput.value,
        level: parseInt(charLevelInput.value),
        race: charRaceInput.value,
        class: charClassInput.value,
        stats: {
            str: parseInt(statInputs.str.value),
            dex: parseInt(statInputs.dex.value),
            con: parseInt(statInputs.con.value),
            int: parseInt(statInputs.int.value),
            wis: parseInt(statInputs.wis.value),
            cha: parseInt(statInputs.cha.value)
        },
        inventory: inventory
    };
    
    if (editMode && currentCharacterId) {
        updateCharacter(currentCharacterId, data);
    } else {
        createCharacter(data);
    }
    
    closeModal(characterModal);
});

btnCancel.addEventListener('click', () => closeModal(characterModal));

btnDiceRoll.addEventListener('click', rollDice);
document.getElementById('btnRollAgain').addEventListener('click', rollDice);

document.getElementById('btnEditFromDetails').addEventListener('click', () => {
    const char = characters.find(c => c.id === currentCharacterId);
    if (!char) return;
    
    editMode = true;
    charNameInput.value = char.name;
    charLevelInput.value = char.level;
    charRaceInput.value = char.race;
    charClassInput.value = char.class;
    
    Object.keys(char.stats).forEach(stat => {
        statInputs[stat].value = char.stats[stat];
    });
    updateModifiers();
    
    inventoryList.innerHTML = '';
    char.inventory.forEach(item => {
        const tag = document.createElement('div');
        tag.className = 'inventory-tag';
        tag.innerHTML = `
            ${item}
            <span class="remove">×</span>
        `;
        tag.querySelector('.remove').addEventListener('click', () => tag.remove());
        inventoryList.appendChild(tag);
    });
    
    modalTitle.textContent = `Edit ${char.name}`;
    closeModal(detailsModal);
    openModal(characterModal);
});

document.getElementById('btnDeleteFromDetails').addEventListener('click', () => {
    deleteCharacter(currentCharacterId);
});

document.getElementById('btnConfirmDelete').addEventListener('click', async () => {
    try {
        const response = await fetch(`/api/characters/${deleteCharacterId}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) throw new Error('Failed to delete character');
        
        showSuccess('Character deleted successfully!');
        fetchCharacters();
        closeModal(deleteModal);
        closeModal(detailsModal);
    } catch (error) {
        showError(error.message);
    }
});

document.getElementById('btnCancelDelete').addEventListener('click', () => {
    closeModal(deleteModal);
});

document.getElementById('btnCloseDetails').addEventListener('click', () => {
    closeModal(detailsModal);
});

// Close modals on close button
document.querySelectorAll('.close').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const modal = e.target.closest('.modal');
        if (modal) closeModal(modal);
    });
});

// Close modals on outside click
window.addEventListener('click', (e) => {
    if (e.target === characterModal) closeModal(characterModal);
    if (e.target === detailsModal) closeModal(detailsModal);
    if (e.target === diceModal) closeModal(diceModal);
    if (e.target === deleteModal) closeModal(deleteModal);
    if (e.target === document.getElementById('loadDataWarningModal')) closeModal(document.getElementById('loadDataWarningModal'));
});

// Search
searchBox.addEventListener('input', (e) => {
    const keyword = e.target.value.toLowerCase();
    if (!keyword) {
        renderCharacters(characters);
        return;
    }
    
    const filtered = characters.filter(char =>
        char.name.toLowerCase().includes(keyword) ||
        char.race.toLowerCase().includes(keyword) ||
        char.class.toLowerCase().includes(keyword)
    );
    renderCharacters(filtered);
});

// Update modifiers when stats change
Object.values(statInputs).forEach(input => {
    input.addEventListener('change', updateModifiers);
});

// Initialize
fetchCharacters();
updateModifiers();
