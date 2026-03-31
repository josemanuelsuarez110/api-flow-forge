document.addEventListener('DOMContentLoaded', async () => {
    const grid = document.getElementById('product-grid');
    const totalStat = document.getElementById('stat-total');
    const valueStat = document.getElementById('stat-value');
    const premiumStat = document.getElementById('stat-premium');

    try {
        // Fetch the processed JSON data
        // Note: In local development, you might need a local server (like Live Server or python -m http.server)
        const response = await fetch('data/processed/products_processed.json');
        
        if (!response.ok) {
            throw new Error('Dataset not found. Please run the ETL pipeline first.');
        }

        const data = await response.json();
        renderDashboard(data);

    } catch (error) {
        console.error(error);
        grid.innerHTML = `
            <div class="loading">
                <p>Dataset not found or error loading data.</p>
                <p style="font-size: 0.9rem; margin-top: 1rem;">Action required: Run <code>python app/main.py</code> locally to generate results.</p>
            </div>
        `;
    }

    function renderDashboard(products) {
        // Update Stats
        const totalValue = products.reduce((acc, p) => acc + p.inventory_value, 0);
        const premiumCount = products.filter(p => p.rating_class === 'Premium').length;

        totalStat.textContent = products.length;
        valueStat.textContent = `$${(totalValue / 1000).toFixed(1)}k`;
        premiumStat.textContent = premiumCount;

        // Clear Grid
        grid.innerHTML = '';

        // Render Cards
        products.forEach(p => {
            const card = document.createElement('div');
            card.className = 'product-card glass';
            
            const badgeClass = p.rating_class === 'Premium' ? 'badge-premium' : 'badge-other';

            card.innerHTML = `
                <img src="${p.thumbnail}" alt="${p.name}" class="product-image" onerror="this.src='https://via.placeholder.com/400x200?text=Product+Image'">
                <div class="product-info">
                    <span class="badge ${badgeClass}">${p.rating_class} Rating</span>
                    <h3>${p.name}</h3>
                    <p style="font-size: 0.875rem; color: #94a3b8; margin-bottom: 0.5rem;">${p.brand} | ${p.category}</p>
                    <div class="price-row">
                        <span class="price">$${p.final_price}</span>
                        <span class="stock">${p.stock_quantity} in stock</span>
                    </div>
                </div>
            `;
            grid.appendChild(card);
        });
    }
});
