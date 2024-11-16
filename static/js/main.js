// API URLlari
const searchApiUrl = "https://arzonlab.uz/api/types/search/";
const analyseApiUrl = "https://arzonlab.uz/api/analyses/";

// HTTPS yo'naltirish (localhostdan tashqari)
if (window.location.protocol === 'http:' && !window.location.host.includes('localhost')) {
    window.location.href = window.location.href.replace('http:', 'https:');
}

// Type qidirish funksiyasi
function searchType() {
    const searchText = document.getElementById('searchText').value;

    if (!searchText.trim()) {
        alert('Iltimos, qidiriladigan matnni kiriting!');
        return;
    }

    const typeResultDiv = document.getElementById('typeResult');
    typeResultDiv.innerHTML = '<p>Qidirilmoqda...</p>'; // Loading xabarini ko'rsatish

    // APIga so'rov yuborish
    fetch(`${searchApiUrl}${searchText}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Tahlil topilmadi');
            }
            return response.json();
        })
        .then(data => {
            typeResultDiv.innerHTML = ''; // Oldingi loading xabarini tozalash

            // data.results arrayga tekshirish
            if (!Array.isArray(data.results)) {
                throw new Error('Kutilmagan javob formati');
            }

            if (data.results.length === 0) {
                typeResultDiv.innerHTML = '<p>Bunday tahlil topilmadi</p>';
                return;
            }

            const list = document.createElement('ul');
            data.results.forEach(item => {
                const listItem = document.createElement('li');
                listItem.innerHTML = `ID: ${item.id}<br> Nomi: ${item.name}<br> Narxi: ${item.price}<br> Ma'lumot: ${item.info}<br> Tayyor bo'lish vaqti: ${item.to_be_ready} kun`;
                list.appendChild(listItem);
            });
            typeResultDiv.appendChild(list);
        })
        .catch(error => {
            typeResultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}

// Analyse ma'lumotini olish funksiyasi
function getAnalysis() {
    const analyseId = document.getElementById('analyseId').value;

    if (!analyseId.trim()) {
        alert('Laboratoriya tomonidan berilgan IDni kiriting!');
        return;
    }

    const analyseResultDiv = document.getElementById('analyseResult');
    analyseResultDiv.innerHTML = '<p>Yuklanmoqda...</p>'; // Loading xabarini ko'rsatish

    // APIga so'rov yuborish
    fetch(`${analyseApiUrl}${analyseId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Tahlil topilmadi');
            }
            return response.json();
        })
        .then(data => {
            analyseResultDiv.innerHTML = ''; // Oldingi loading xabarini tozalash

            const analyseDiv = document.createElement('div');
            analyseDiv.classList.add('result');

            analyseDiv.innerHTML = `
                <h3>Analysis ID: ${data.id}</h3>
                <p><strong>Tahlil tayyor bo'lgan vaqt:</strong> ${new Date(data.created_at).toLocaleString()}</p>
                <a href="${data.file}" target="_blank">PDF Yuklab olish</a>
            `;

            analyseResultDiv.appendChild(analyseDiv);
        })
        .catch(error => {
            analyseResultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}
